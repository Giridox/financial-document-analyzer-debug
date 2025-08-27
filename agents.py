import os
from dotenv import load_dotenv
load_dotenv()

from crewai.agents.agent_builder.base_agent import BaseAgent
from tools import search_tool, FinancialDocumentTool

from crewai.llms import OpenAI
llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Your LLM setup


class FinancialAnalystAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Financial Analyst",
            description="Experienced Financial Analyst who provides evidence-based financial advice.",
            role="Experienced Financial Analyst",
            goal="Provide clear, evidence-based investment advice and insights on user financial queries.",
            verbose=True,
            memory=True,
            backstory=(
                "You are a senior financial analyst with a strong background in market research, "
                "risk analysis, and investment recommendations. You carefully analyze financial documents, "
                "respect regulatory guidelines, and provide actionable insights using professional judgement."
            ),
            llm=llm,
            tools=[FinancialDocumentTool.read_data_tool],
            max_iter=3,
            max_rpm=2,
            allow_delegation=True,
        )

    async def run(self, input_data):
        # Implement your custom agent logic here
        # For now, this is a simple placeholder returning input summary
        return f"Analyzing financial data with input: {input_data}"


class VerifierAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Financial Document Verifier",
            description="Verifies whether uploaded documents are genuine financial reports.",
            role="Financial Document Verifier",
            goal="Verify whether uploaded documents are genuine financial reports and check for key compliance features.",
            verbose=True,
            memory=True,
            backstory=(
                "As a former financial compliance officer, you are detail-oriented and ensure that all documents "
                "adhere to reporting and regulatory standards."
            ),
            llm=llm,
            tools=[FinancialDocumentTool.read_data_tool],
            max_iter=2,
            max_rpm=1,
            allow_delegation=False,
        )

    async def run(self, input_data):
        # Verification logic placeholder
        return "Document verified as valid financial report."


class InvestmentAdvisorAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Investment Advisor",
            description="Recommends investment products and strategies based on analysis.",
            role="Investment Advisor",
            goal="Recommend suitable investment products and strategies based on detailed analysis.",
            verbose=True,
            backstory=(
                "Driven by a knack for detecting market trends and opportunities, you guide investors to "
                "risk-adjusted investment choices with consideration for client needs."
            ),
            llm=llm,
            tools=[FinancialDocumentTool.read_data_tool],
            max_iter=2,
            max_rpm=1,
            allow_delegation=False,
        )

    async def run(self, input_data):
        # Placeholder for investment advice generation
        return "Recommended investment products based on analysis."


class RiskAssessorAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Risk Assessment Specialist",
            description="Evaluates financial risks based on document evidence.",
            role="Risk Assessment Specialist",
            goal="Accurately evaluate investment and financial risks based on document evidence.",
            verbose=True,
            backstory=(
                "A seasoned risk analyst, you identify, quantify, and communicate risks using industry standards and "
                "empirical data, providing rational recommendations."
            ),
            llm=llm,
            tools=[FinancialDocumentTool.read_data_tool],
            max_iter=2,
            max_rpm=1,
            allow_delegation=False,
        )

    async def run(self, input_data):
        # Placeholder for risk assessment
        return "Provided detailed risk assessment."

# Instantiate agent objects for use in your Crew
financial_analyst = FinancialAnalystAgent()
verifier = VerifierAgent()
investment_advisor = InvestmentAdvisorAgent()
risk_assessor = RiskAssessorAgent()
