from crewai import Crew, Process
from agents import financial_analyst, verifier, investment_advisor, risk_assessor
from task import analyze_financial_document, verification, investment_analysis, risk_assessment

def create_financial_crew():
    """
    Create and return a Crew instance configured with financial document
    analysis agents and tasks.
    """
    # You can choose to run tasks sequentially or in parallel
    process_type = Process.sequential  # or Process.parallel
    
    financial_crew = Crew(
        agents=[financial_analyst, verifier, investment_advisor, risk_assessor],
        tasks=[analyze_financial_document, verification, investment_analysis, risk_assessment],
        process=process_type,
        verbose=True,
    )
    
    return financial_crew
