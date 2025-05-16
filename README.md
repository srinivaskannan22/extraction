# Data Extraction Backend using FastAPI

This project provides a backend service for extracting data from various file formats such as JPG, PDF, XLSX, DOCX, and CSV. The backend is built using **FastAPI** and integrates several powerful libraries for data extraction, including **Pillow**, **PDFPlumber**, **Pytesseract**, **Tabulate**, **Python-Doctr**, **OpenPyXL**, **Docx2Txt**, and more.

## Libraries Used

- **FastAPI**: High-performance web framework for building APIs.
- **Pillow**: Image processing for handling JPG files.
- **PDFPlumber**: PDF text extraction.
- **Pytesseract**: Optical Character Recognition (OCR) for text extraction from images.
- **Tabulate**: For pretty-printing tabular data in the response.
- **Python-Doctr**: For document parsing and conversion.
- **OpenPyXL**: To handle reading and writing Excel files.
- **Docx2Txt**: To extract text from DOCX files.
- **Python-Multipart**: For file handling in HTTP requests.
- **Uvicorn**: ASGI server to run FastAPI.
- **Streamlit**: For building a simple front-end interface to interact with the backend.
- **HTTPX**: For making asynchronous HTTP requests.
- **Asyncio**: To support asynchronous operations.

## Features

- **JPG File Extraction**: Extracts text from images using **Pytesseract**.
- **PDF File Extraction**: Extracts text and tables from PDFs using **PDFPlumber**.
- **XLSX File Extraction**: Reads data from Excel files using **OpenPyXL**.
- **DOCX File Extraction**: Extracts text from DOCX files using **Docx2Txt**.
- **CSV File Extraction**: Reads and processes data from CSV files using **Pandas**.

## Setup and Installation

1. **Clone the repository**:

   ```bash
   git clone  git@github.com:BootlabsAI/data_extraction_backend.git
   cd data_extraction_backend

2. **Create a virtual environment**:

```bash
python -m venv venv
source venv/bin/activate 
On Windows, use venv\Scripts\activate
``` 



3. **Install dependencies**:

```bash

pip install -r requirements.txt
```

**Install Tesseract (for OCR):**

Download and install Tesseract from: Tesseract OCR

Ensure tesseract is available in your system’s PATH.

Running the Application
To run the FastAPI backend:

```bash
uvicorn main:app --reload
This will start the server at http://127.0.0.1:8000.
```

Streamlit Frontend
The frontend is built using Streamlit and provides an easy-to-use interface for uploading files and displaying the extracted data.

How to Launch the Streamlit UI
Run the Streamlit app:

```bash
streamlit run frontend_loader.py
```
This will launch the UI in your browser. The default address is http://localhost:8501.

Streamlit Interface Features
File Upload: Upload files in JPG, PDF, XLSX, DOCX, or CSV format.

Display Results: View the extracted text from the uploaded files. For images (JPG), the text is extracted via OCR. For PDFs, DOCX, and CSV files, text and tabular data are shown in the UI.

Easy Navigation: The UI includes buttons to upload files and automatically fetch results for each supported format.

Example Flow
Upload a JPG file: Streamlit will allow you to select and upload an image, after which Pytesseract will be used to extract the text from the image.

Upload a PDF file: Once uploaded, PDFPlumber will extract the text and tables from the PDF.

Upload an XLSX or CSV file: The app will read the content of the file and display it as a table using OpenPyXL or Pandas.

Upload a DOCX file: The text will be extracted from the document using Docx2Txt.

Example Request using the Streamlit Interface
After running the Streamlit app, navigate to the provided link in your browser. You will see the following:

A button to Upload Files.

An option to choose files from your computer, which will be processed by the backend.

A display section where the extracted data (text or table) will be shown.

API Endpoints
Upload JPG for Text Extraction:

POST /extract/jpg/

File: A JPG file to extract text from.

Upload PDF for Text Extraction:

POST /extract/pdf/

File: A PDF file to extract text from.

Upload XLSX for Data Extraction:

POST /extract/xlsx/

File: An XLSX file to extract data from.

Upload DOCX for Text Extraction:

POST /extract/docx/

File: A DOCX file to extract text from.

Upload CSV for Data Extraction:

POST /extract/csv/

File: A CSV file to extract data from.

Example Request using curl:
```
curl -X 'POST' \
  'http://127.0.0.1:8000/extract/jpg/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@/path/to/your/image.jpg'

```

Contributing
Fork the repository.



### Key Changes:

1. **Streamlit UI Section**: Added a section for Streamlit UI, explaining how to run it and its features.
2. **Frontend Interaction**: Clear description of the file upload and display features available in the UI.
3. **Example Flow**: Demonstrated how the UI works with various file types (JPG, PDF, DOCX, etc.).

