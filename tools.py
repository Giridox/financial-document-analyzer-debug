# tools.py - FIXED VERSION
from crewai.tools import BaseTool
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()

class FinancialDocumentAnalyzer(BaseTool):
    name: str = "Financial Document Analyzer"
    description: str = "Analyzes financial documents and extracts key information"

    def _run(self, document_path: str) -> str:
        '''Analyze a financial document and return key insights'''
        # Your document analysis logic here
        try:
            # Process the document
            result = f"Analysis of {document_path} completed"
            return result
        except Exception as e:
            return f"Error analyzing document: {str(e)}"

class PDFReaderTool(BaseTool):
    name: str = "PDF Reader"
    description: str = "Reads and extracts text from PDF files"

    def _run(self, pdf_path: str) -> str:
        '''Read PDF file and return text content'''
        try:
            # PDF reading logic here
            return f"Text extracted from {pdf_path}"
        except Exception as e:
            return f"Error reading PDF: {str(e)}"
