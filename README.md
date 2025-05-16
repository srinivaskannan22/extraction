# Data Extraction Backend using FastAPI
This project provides a backend service for extracting data from various file formats such as JPG, PDF, XLSX, DOCX, and CSV. The backend is built using FastAPI and integrates several powerful libraries for data extraction, including Pillow, PDFPlumber, Pytesseract, Tabulate, Python-Doctr, OpenPyXL, Docx2Txt, and more.

## Libraries Used

FastAPI: High-performance web framework for building APIs.

Pillow: Image processing for handling JPG files.

PDFPlumber: PDF text extraction.

Pytesseract: OCR for extracting text from images.

Tabulate: Pretty-prints tables in responses.

Python-Doctr: Intelligent document parsing.

OpenPyXL: Reads and writes Excel files.

Docx2Txt: Extracts text from DOCX documents.

Pandas: Processes CSV files.

Python-Multipart: Handles file uploads.

Uvicorn: ASGI server for FastAPI.

Streamlit: Frontend interface for easy file uploads.

HTTPX: For asynchronous HTTP requests.

Asyncio: Enables async programming.

uv: A fast Python package and environment manager.

## Features
🖼️ JPG OCR: Extracts text from images using Pytesseract.

📄 PDF Parsing: Extracts text and tables using PDFPlumber.

📊 XLSX Extraction: Extracts data from Excel spreadsheets.

📝 DOCX Parsing: Extracts raw text from Word documents.

📂 CSV Handling: Reads and displays tabular CSV data.

⚙️ Setup & Installation (with uv)
Prerequisites: Python 3.8+ and uv must be installed.

1. ### Clone the repository
```bash
git clone git@github.com:BootlabsAI/data_extraction_backend.git
cd data_extraction_backend
```
### 2. Create a virtual environment and install dependencies
```bash
uv venv
source .venv/bin/activate     # On Windows: .venv\Scripts\activate
uv pip install .
```

### 3. Install Tesseract (Required for OCR)
```bash
Download and install from Tesseract OCR

Ensure the tesseract executable is available in your system PATH.
```

### ▶️ Running the Application
#### Run the FastAPI Backend
```bash
uvicorn main:app --reload
Visit the API docs at: http://127.0.0.1:8000/docs

```

### 🖥️ Streamlit Frontend
A lightweight UI built with Streamlit allows you to interact with the backend and visualize extracted data.

Launch the Streamlit App
```bash
streamlit run frontend_loader.py
Visit: http://localhost:8501

```

🌐 Streamlit Interface Features
File Upload: Upload JPG, PDF, XLSX, DOCX, or CSV files.

Text and Table Extraction: Extracted data is displayed based on file type.

Interactive UI: Upload files and get results with one click.

### 🧪 Example Flow
JPG Upload: Text is extracted using OCR (Pytesseract).

PDF Upload: Text and tables are parsed using PDFPlumber.

XLSX/CSV Upload: Data is displayed as a formatted table.

DOCX Upload: Extracted text appears directly in the UI.

### 📦 API Endpoints
Endpoint	Method	File Type	Description
/file_extraction	POST	JPG	Extracts text from an image
/file_extraction	POST	PDF	Extracts text and tables
/file_extraction	POST	XLSX	Reads data from Excel files
/file_extraction	POST	DOCX	Extracts text from Word docs
/file_extraction	POST	CSV	Displays CSV content

### 🔧 Example API Request (via curl)

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/extract/jpg/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@/path/to/your/image.jpg'
```



