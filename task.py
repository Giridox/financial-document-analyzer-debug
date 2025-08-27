from crewai import Task
from agents import financial_analyst, verifier, investment_advisor, risk_assessor
from tools import FinancialDocumentTool

## Task: Analyze financial document for insights
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
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

## Task: Verify the authenticity and relevance of the financial document
verification = Task(
    description=(
        "Verify if the uploaded document is a valid financial report. "
        "Check for compliance and key financial indicators."
    ),
    expected_output=(
        "Confirm document validity or highlight discrepancies."
    ),
    agent=verifier,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

## Task: Provide investment product recommendations based on analysis
investment_analysis = Task(
    description=(
        "Analyze financial data and user queries to recommend "
        "investment products and strategies."
    ),
    expected_output=(
        "List suitable investment options supported by financial data."
    ),
    agent=investment_advisor,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

## Task: Perform risk assessment for investments and market conditions
risk_assessment = Task(
    description=(
        "Evaluate risk factors and potential volatility based on financial data."
    ),
    expected_output=(
        "Provide detailed risk analysis and mitigation recommendations."
    ),
    agent=risk_assessor,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)
