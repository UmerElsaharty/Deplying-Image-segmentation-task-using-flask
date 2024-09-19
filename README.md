# Deplying-Image-segmentation-task-using-flask

This repository contains a Flask application for performing image segmentation using a pre-trained U-Net model. The app allows users to upload `.tif` images, processes the uploaded image by extracting the RGB channels, predicts a segmentation mask using the U-Net model, overlays the mask on the original image, and returns the result back to the user in the browser.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- Upload `.tif` images with multiple channels.
- Extracts RGB channels (3, 2, 1) from the 12-channel images.
- Preprocesses the image to the required format for the model.
- Applies a pre-trained U-Net model for image segmentation.
- Overlays the predicted segmentation mask onto the RGB image.
- Displays the resulting overlaid image in the browser for download.
  
## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- `pip` (Python package manager)
- `virtualenv` (recommended for creating an isolated environment)

### Clone the Repository
```bash
git clone https://github.com/UmerElsaharty/Deplying-Image-segmentation-task-using-flask.git
cd Deplying-Image-segmentation-task-using-flask
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On MacOS/Linux:
source venv/bin/activate
```
### Install Dependencies
```bash
pip install -r requirements.txt
```
### Add Your Model 
Ensure that the U-Net model file model.h5 is placed in the appropriate folder (specified in the code as MODEL_PATH). You can modify the path if necessary in the app.py file.

### Create Uploads Folder

```bash
mkdir uploads

```
## Usage
### Run the flask app 
```bash
python app.py
```
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
└── README.md               # Project readme file
```
## Contributing
Contributions are welcome! Please feel free to submit a Pull Request if you have any suggestions or improvements.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
