from crewai import Task
from agents import financial_analyst, document_processor
from tools import FinancialDocumentAnalyzer


# Task to analyze financial document for insights using the financial analyst agent
analyze_financial_document = Task(
    description=(
        "Analyze the user's query regarding a financial document. "
        "Use financial knowledge and tools to provide meaningful insights, "
        "including investment recommendations and risk factors."
    ),
    expected_output=(
        "Provide detailed financial analysis, market risks, and investment advice "
        "based on data from the financial document."
    ),
    agent=financial_analyst,
    tools=[FinancialDocumentAnalyzer()],
    async_execution=False,
)


# Task to process financial documents for structured data extraction
process_financial_document = Task(
    description=(
        "Process and extract structured data from financial documents. "
        "Ensure data cleanliness and organization for further analysis."
    ),
    expected_output=(
        "Extract structured financial data suitable for analysis."
    ),
    agent=document_processor,
    tools=[FinancialDocumentAnalyzer()],
    async_execution=False,
)
