import os
from dotenv import load_dotenv

load_dotenv()

from crewai_tools import tools
from crewai_tools.tools.pdf_tool import Pdf  # Correct import of PDF loader
from crewai_tools.tools.serper_dev_tool import SerperDevTool

# Creating search tool instance
search_tool = SerperDevTool()

class FinancialDocumentTool:
    @staticmethod
    async def read_data_tool(path='data/sample.pdf'):
        """Tool to read data from a pdf file from a path

        Args:
            path (str, optional): Path of the pdf file. Defaults to 'data/sample.pdf'.

        Returns:
            str: Full financial document text
        """
        docs = Pdf(file_path=path).load()
        full_report = ""
        for data in docs:
            content = data.page_content
            # Clean extra whitespaces and format properly
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")
            full_report += content + "\n"
        return full_report

class InvestmentTool:
    @staticmethod
    async def analyze_investment_tool(financial_document_data):
        # Process and analyze the financial document data (placeholder)
        processed_data = financial_document_data.replace("  ", " ")  # simple cleanup
        # TODO: implement real investment analysis logic
        return "Investment analysis functionality to be implemented."

class RiskTool:
    @staticmethod
    async def create_risk_assessment_tool(financial_document_data):
        # TODO: implement real risk assessment logic
        return "Risk assessment functionality to be implemented."
