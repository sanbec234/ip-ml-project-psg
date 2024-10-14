# CUSTOM TRAINED YOLOv7

THIS PROJECT IS FOR ELECTRIC UTILITY POLE DETECTION TRAINED USING CUSTOM DATASET

# STEPS TO RUN

1. Install requirements from "requirements.txt" and "requirements_GPU.txt"
2. run main.py using "python main.py"

# Flask File Upload with Detection Script

This project is a web application built with Flask that allows users to upload files (images or videos) and runs a detection script (`flaskdetect.py`) on the uploaded files. The app uses Flask-WTF for form handling and integrates subprocess to execute a Python script (`flaskdetect.py`) with custom arguments.

## Features

- **File Upload**: Users can upload files (images or videos).
- **Script Execution**: After a file is uploaded, the app runs the `flaskdetect.py` script with custom arguments (e.g., weights, confidence, and image size).
- **File Display**: After processing, the file is displayed on a separate page.

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML (Flask templates)
- **Form Handling**: Flask-WTF (WTForms)
- **File Upload**: FileField (WTForms), secure_filename (Werkzeug)
- **Script Execution**: Subprocess
- **File Serving**: Static folder for storing uploaded files

## Setup Instructions

### Prerequisites

- Python 3.x
- Flask
- Flask-WTF
- WTForms
- Werkzeug

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/flask-upload-detection.git
    cd flask-upload-detection
    ```

2. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Add Your Detection Script**:
    - Place your `flaskdetect.py` script in the root directory of the project.
    - This script should accept the following arguments: `--weights`, `--conf`, `--img-size`, `--source`, `--view-img`, `--no-trace`.

4. **Configure Uploads Folder**:
    - By default, uploaded files will be saved in the `static/files` directory. You can change this in the `app.config['UPLOAD_FOLDER']` variable.

5. **Run the Application**:
    ```bash
    python app.py
    ```

6. **Access the Application**:
    - Open your browser and navigate to `http://localhost:5000`.

## Usage

1. **Upload a File**:
   - Navigate to the homepage (`/` or `/home`).
   - Upload an image or video file using the form.
   
2. **Run the Detection Script**:
   - After the file is uploaded, the app automatically runs `flaskdetect.py` with the specified arguments.
   
3. **View the Uploaded File**:
   - After the script finishes processing, you will be redirected to a page where the uploaded file is displayed.

## Example

1. **Upload File**: Select an image file and click "Upload".
2. **Processing**: The app will run the detection script on the file using the following command format:
    ```bash
    python flaskdetect.py --weights best.pt --conf 0.5 --img-size 640 --source static/files/<filename> --view-img --no-trace
    ```
3. **View File**: After processing, the file will be displayed in your browser.

## Folder Structure
flask-upload-detection/ │ ├── app.py # Main Flask app
├── flaskdetect.py # Detection script
├── templates/
│ └── index.html # Template for the home page with file upload form
├── static/
│ └── files/ # Folder where uploaded files are stored
└── requirements.txt # Dependencies

## Dependencies

- **Flask**: Web framework for Python
- **Flask-WTF**: WTForms integration with Flask
- **WTForms**: Form handling and validation
- **Werkzeug**: Utilities for secure filename handling
- **Subprocess**: For executing external scripts

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request. All contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

