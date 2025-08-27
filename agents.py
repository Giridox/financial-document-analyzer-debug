import os
from dotenv import load_dotenv
load_dotenv()
from crewai.agents import Agent
from tools import search_tool, FinancialDocumentTool

# Import or initialize your chosen LLM for agents (e.g., OpenAI)
from crewai.llms import OpenAI
llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Or your LLM setup

financial_analyst = Agent(
    role="Experienced Financial Analyst",
    goal="Provide clear, evidence-based investment advice and insights on user financial queries.",
    verbose=True,
    memory=True,
    backstory=(
        "You are a senior financial analyst with a strong background in market research, "
        "risk analysis, and investment recommendations. You carefully analyze financial documents, "
        "respect regulatory guidelines, and provide actionable insights using professional judgement."
    ),
    tools=[FinancialDocumentTool.read_data_tool],  # use correctly imported/read tool
    llm=llm,
    max_iter=3,
    max_rpm=2,
    allow_delegation=True
)

verifier = Agent(
    role="Financial Document Verifier",
    goal="Verify whether uploaded documents are genuine financial reports and check for key compliance features.",
    verbose=True,
    memory=True,
    backstory=(
        "As a former financial compliance officer, you are detail-oriented and ensure that all documents "
        "adhere to reporting and regulatory standards."
    ),
    tools=[FinancialDocumentTool.read_data_tool],
    llm=llm,
    max_iter=2,
    max_rpm=1,
    allow_delegation=False
)

investment_advisor = Agent(
    role="Investment Advisor",
    goal="Recommend suitable investment products and strategies based on detailed analysis.",
    verbose=True,
    backstory=(
        "Driven by a knack for detecting market trends and opportunities, you guide investors to "
        "risk-adjusted investment choices with consideration for client needs."
    ),
    tools=[FinancialDocumentTool.read_data_tool],
    llm=llm,
    max_iter=2,
    max_rpm=1,
    allow_delegation=False
)

risk_assessor = Agent(
    role="Risk Assessment Specialist",
    goal="Accurately evaluate investment and financial risks based on document evidence.",
    verbose=True,
    backstory=(
        "A seasoned risk analyst, you identify, quantify, and communicate risks using industry standards and "
        "empirical data, providing rational recommendations."
    ),
    tools=[FinancialDocumentTool.read_data_tool],
    llm=llm,
    max_iter=2,
    max_rpm=1,
    allow_delegation=False
)
