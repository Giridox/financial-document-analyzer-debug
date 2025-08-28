# Financial Document Analyzer

## Project Overview
A comprehensive financial document analysis system that processes corporate reports, financial statements, and investment documents using AI-powered analysis agents and an integrated database backend.

---

## Features Implemented
- Upload financial documents (PDF format) via API
- AI-powered financial analysis with CrewAI and OpenAI integration
- Persistent storage of documents and analysis results using MySQL database
- Automated tests to validate API endpoints and functionality
- Secure environment variable management for API keys
- Cleaned Git history to avoid leaking secrets
- Detailed error handling and cleanup for file uploads

---

## Getting Started

### Prerequisites
- Python 3.10+
- MySQL database running (can be via Docker)
- OpenAI API key configured securely via `.env`

### Install Required Libraries
pip install -r requirements.txt

### Database Setup
1. Run MySQL (e.g., via Docker):
docker run --name financial_db -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=financial_docs -p 3306:3306 -d mysql:8

2. Initialize database tables:
python init_db.py

### Sample Document for Testing
The project includes a sample Tesla Q2 2025 financial update PDF in the `data` folder (`data/TSLA-Q2-2025-Update.pdf`).

---

## Usage

### API Endpoints

- `POST /analyze-document/`  
Upload a PDF file to analyze and receive extracted financial insights.

- `GET /`  
Basic health check endpoint with welcome message.

- `GET /health`  
API health status endpoint.

---

## Testing

- Automated tests are provided in `test_main.py` covering API endpoints and file uploads.
- Use pytest to run tests:

pytest test_main.py

---

## Environment Variables

- Use a `.env` file to securely store your OpenAI API keys and database credentials.
- The project uses `python-dotenv` to load environment variables.

---

## Notes & Recommendations

- Asynchronous job handling, frontend UI, and CI/CD pipelines are planned next steps but are not currently implemented to keep the system simple and maintainable.
- Avoid committing `.env` files or any secrets to version control.
- The project uses SQLAlchemy with MySQL via Docker for persistent data storage.
- Tests mock or reduce external AI dependencies for consistent test runs without exhausting API quotas.

---

## Acknowledgements
- Powered by FastAPI, CrewAI, PyMuPDF, SQLAlchemy, and OpenAI API.
- Thanks to the open source community for all the supporting packages.

---

## Contact / Support
Feel free to open issues or pull requests via the GitHub repository.

Happy analyzing! 🚀
