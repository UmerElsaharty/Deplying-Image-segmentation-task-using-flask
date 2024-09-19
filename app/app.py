from flask import Flask, render_template, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
import os
from keras import  models
from keras.models import load_model
import cv2
import numpy as np
import imageio
import tensorflow as tf
# Initialize Flask app
app = Flask(__name__)

# Load your U-Net model
MODEL_PATH = r"Path to the model"  # Path to the model
model = load_model(MODEL_PATH, compile=False)

# Define the directory to save uploaded images
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Allowed image extensions
ALLOWED_EXTENSION = {"tif"}


# Check if uploaded file is allowed
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSION


# Preprocess the input image (using imageio for tif support)
def preprocess_image(image_path):
    extension = image_path.rsplit(".", 1)[1].lower()

    if extension == 'tif':
        img = imageio.imread(image_path)  # Load tif images with imageio
    else:
        raise ValueError("Please, upload only tif images")
    
    # Extract only the RGB channels 
    rgb_img = img[:, :, [1, 2, 3]]

    # Normalize the RGB channels to the range [0, 255]
    rgb_img = rgb_img.astype(np.float32)  # Ensure it's float32 for scaling
    rgb_img -= rgb_img.min()  # Subtract the minimum value to shift to 0
    rgb_img /= rgb_img.max()  # Scale to [0, 1]
    rgb_img *= 255.0  # Scale to [0, 255]
    rgb_img = rgb_img.astype(np.uint8)  # Convert to uint8
    
    # Resize the RGB image to match the model input size
    rgb_img_resized = cv2.resize(rgb_img, (128, 128))
    
    # Resize the full image (including all 12 channels) for model input
    img_resized = cv2.resize(img, (128, 128))

    return img_resized, rgb_img_resized  # Return both resized full image and RGB image



# Post-process the model output
def postprocess_output(output):
    output = np.squeeze(output)  # Remove extra dimensions
    output = (output > 0.5).astype(np.uint8)  # Convert to binary mask
    return output

# Overlay the predicted binary mask on the RGB image
def overlay_mask_on_image(rgb_img, mask):
    # Ensure mask is resized to match the RGB image
    mask_resized = cv2.resize(mask, (rgb_img.shape[1], rgb_img.shape[0]))  
    
    # Convert binary mask to RGB by stacking it 3 times to match the RGB image shape
    mask_rgb = np.stack([mask_resized]*3, axis=-1)*255
    
    # Convert the mask to uint8 type and multiply by 255 to make it binary
    mask_rgb = mask_rgb.astype(np.uint8)
    
    # Ensure both the RGB image and mask are uint8
    rgb_img = rgb_img.astype(np.uint8)
    
    # Overlay the mask on the RGB image (blend the two images)
    overlay = cv2.addWeighted(rgb_img, 0.5, mask_rgb, 0.5, 0)
    
    return overlay


# Route to handle the main page
@app.route("/", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        # Check if a file was uploaded
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]

        # If a valid file is uploaded
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(file_path)

            # Preprocess the image and get predictions
            img, rgb_img = preprocess_image(file_path)
            prediction = model.predict(tf.expand_dims(img, axis=0))

            # Post-process the prediction
            mask = postprocess_output(prediction)

            # Overlay the mask on the RGB image
            overlay_img = overlay_mask_on_image(rgb_img, mask)

            # Save the overlay image
            overlay_filename = f"overlay_{filename.rsplit('.', 1)[0]}.png"
            overlay_path = os.path.join(app.config["UPLOAD_FOLDER"], overlay_filename)
            cv2.imwrite(overlay_path, overlay_img)

            # Send the result to the browser
            return send_file(overlay_path, mimetype="image/png")

    return render_template("index.html")


# Run the app
if __name__ == "__main__":
    app.run(debug=True)

