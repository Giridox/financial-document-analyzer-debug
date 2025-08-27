import os
from dotenv import load_dotenv

load_dotenv()

from crewai_tools import tools
from crewai_tools.tools.pdf_tool import Pdf  # Proper import of PDF loader
from crewai_tools.tools.serper_dev_tool import SerperDevTool

# Creating search tool instance
search_tool = SerperDevTool()

class FinancialDocumentTool:
    @staticmethod
    async def read_data_tool(path='data/sample.pdf'):
        """Tool to read data from a pdf file from a given path.

        Args:
            path (str, optional): Path of the pdf file. Defaults to 'data/sample.pdf'.

        Returns:
            str: Full financial document text extracted from PDF.
        """
        docs = Pdf(file_path=path).load()
        full_report = ""
        for data in docs:
            content = data.page_content
            # Remove multiple newlines to clean formatting
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")
            full_report += content + "\n"
        return full_report

class InvestmentTool:
    @staticmethod
    async def analyze_investment_tool(financial_document_data):
        """
        A placeholder function that would analyze financial document data
        and provide investment insights.

        Args:
            financial_document_data (str): Text from a financial document.

        Returns:
            str: Analysis results or summary.
        """
        # Clean up double spaces for demonstration
        processed_data = financial_document_data.replace("  ", " ")
        # TODO: Implement investment analysis logic here
        return "Investment analysis functionality to be implemented."

class RiskTool:
    @staticmethod
    async def create_risk_assessment_tool(financial_document_data):
        """
        A placeholder function that would perform risk assessment
        based on the financial document data.

        Args:
            financial_document_data (str): Text from financial document.

        Returns:
            str: Risk assessment results.
        """
        # TODO: Implement risk assessment logic here
        return "Risk assessment functionality to be implemented."
