# Financial Document Analyzer

## Project Overview

This FastAPI application analyzes financial PDF documents using AI agents powered by CrewAI and OpenAI. Users upload PDFs to extract financial insights for investment and risk assessment.

---

## Features

- Upload PDF documents for financial analysis via API  
- Extract text from PDFs with PyMuPDF  
- AI-driven data extraction and analysis with custom agents and tasks  
- Health check and status endpoints  
- Automated tests for endpoint validation  
- Environment-based OpenAI API key management

---

## Setup Instructions

1. Clone the repo  
2. Create and activate a Python virtual environment  
3. Install dependencies with `pip install -r requirements.txt`  
4. Create a `.env` file with your OpenAI API key:  
OPENAI_API_KEY=your_openai_api_key_here

5. Run the application:  
python main.py

6. Visit [http://localhost:8000/docs](http://localhost:8000/docs) for API docs and testing

---

## API Endpoints

- **GET /** - Basic welcome endpoint  
- **GET /health** - Service health status  
- **POST /analyze-document/** - Upload a PDF file to analyze financial data  

Use multipart/form-data with file upload key `file`. The response returns status, analysis result, and filename.

---

## Bugs Fixed & Improvements

- Fixed incorrect task imports and variable names in `main.py`  
- Fixed file path handling so real uploaded file paths reach agents  
- Added PyMuPDF-based PDF text extraction in tools  
- Added `.env` support for OpenAI API key management  
- Added robust error handling and temp file cleanup  
- Created automated tests for endpoints including file upload test  
- Improved prompt clarity and agent/task consistency

---

## Running Tests

pytest tests.py

Skip slow file upload test by adding:

@pytest.mark.skip(reason="Skipping slow PDF upload")

---

## Next Steps (Bonus Tasks)

- Add queue system (Celery or Redis Queue) for asynchronous request handling  
- Add a database (SQLite, PostgreSQL) to store analysis results and metadata  
- Improve AI prompt engineering for deeper financial insights  
- Develop a frontend UI for user-friendly document uploading and results visualization

---
