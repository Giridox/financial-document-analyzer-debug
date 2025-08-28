from crewai.tools import BaseTool
from typing import Optional
import fitz  # PyMuPDF
from dotenv import load_dotenv
import os

load_dotenv()


class FinancialDocumentAnalyzer(BaseTool):
    name: str = "Financial Document Analyzer"
    description: str = "Analyzes financial documents and extracts key information"

    def _run(self, document_path: str) -> str:
        '''Analyze a financial document and return key insights'''
        try:
            # Open PDF and extract text
            doc = fitz.open(document_path)
            full_text = ""
            for page in doc:
                full_text += page.get_text()

            # Placeholder for more advanced financial document analysis logic
            result_summary = f"Extracted text length: {len(full_text)} characters from {os.path.basename(document_path)}"

            return result_summary
        except Exception as e:
            return f"Error analyzing document: {str(e)}"


class PDFReaderTool(BaseTool):
    name: str = "PDF Reader"
    description: str = "Reads and extracts text from PDF files"

    def _run(self, pdf_path: str) -> str:
        '''Read PDF file and return text content'''
        try:
            doc = fitz.open(pdf_path)
            full_text = ""
            for page in doc:
                full_text += page.get_text()
            return full_text
        except Exception as e:
            return f"Error reading PDF: {str(e)}"
