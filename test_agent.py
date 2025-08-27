from crewai.agents.agent_builder import AgentBuilder

def main():
    # Example minimal AgentBuilder usage (adjust parameters as needed)
    financial_analyst = AgentBuilder(
        name="Financial Analyst",
        description="Analyzes financial data",
        # Add any required parameters your version expects
    ).build()
    
    print("Agent created successfully:", financial_analyst)

if __name__ == "__main__":
    main()
