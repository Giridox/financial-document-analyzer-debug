# agents.py - FIXED VERSION
from crewai import Agent
from crewai.tools import BaseTool
from tools import FinancialDocumentAnalyzer, PDFReaderTool
import os

# Create agent with proper tool initialization
financial_analyst = Agent(
    role='Financial Document Analyst',
    goal='Extract and analyze key financial information from documents',
    backstory='''You are an expert financial analyst with years of experience 
    in analyzing financial documents, reports, and statements. You can identify
    key metrics, trends, and potential issues in financial data.''',
    tools=[FinancialDocumentAnalyzer(), PDFReaderTool()],
    verbose=True,
    allow_delegation=False
)

document_processor = Agent(
    role='Document Processing Specialist',
    goal='Process and organize financial documents for analysis',
    backstory='''You are a document processing expert who specializes in 
    handling various document formats and extracting structured information.''',
    tools=[PDFReaderTool()],
    verbose=True
)
