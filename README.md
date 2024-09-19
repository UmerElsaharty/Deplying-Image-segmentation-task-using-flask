# Deplying-Image-segmentation-task-using-flask

This repository contains a Flask application for performing image segmentation using a pre-trained U-Net model. The app allows users to upload `.tif` images, processes the uploaded image by extracting the RGB channels, predicts a segmentation mask using the U-Net model, overlays the mask on the original image, and returns the result back to the user in the browser.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Upload `.tif` images with multiple channels.
- Extracts RGB channels (3, 2, 1) from the 12-channel images.
- Preprocesses the image to the required format for the model.
- Applies a pre-trained U-Net model for image segmentation.
- Overlays the predicted segmentation mask onto the RGB image.
- Displays the resulting overlaid image in the browser for download.

## Project Structure
```bash

.
├── app.py                  # Main Flask app script
├── model.h5                # Pre-trained U-Net model (add this yourself)
├── requirements.txt        # Python dependencies
├── static
│   └── style.css           # Styles for the app
├── templates
│   └── index.html          # HTML template for the app
├── uploads                 # Directory to store uploaded and processed images
```

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- `pip` (Python package manager)
- `virtualenv` (recommended for creating an isolated environment)

### Install Dependencies
Install Packages used in the app (you can find them in he requirments.txt )
### Add Your Model 
Ensure that the U-Net model file model.h5 is placed in the appropriate folder (specified in the code as MODEL_PATH). You can modify the path if necessary in the app.py file.

## Usage
### Using the terminal after ensuring the correct structure of the app project
```bash
.\venv\Scripts\activate   # activate the virtual environment
cd "path to the app directory"   # go to the app directory
$env:FLASK_APP="app.py"          # file to use as the main application entry point
$env:FLASK_ENV="development"     # run in development mode 
flask run                        # start the Flask development server.
```

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request if you have any suggestions or improvements.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
