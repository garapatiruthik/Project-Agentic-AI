import os
from dotenv import load_dotenv
from langchain_groq import Groq
from langgraph import Graph, State
from state.graph_state import TravelState
from agents.intake_agent import IntakeAgent
from agents.transport_agent import TransportAgent
from agents.accommodation_agent import AccommodationAgent
from agents.experience_agent import ExperienceAgent
from agents.budget_auditor import BudgetAuditor

load_dotenv()

def create_workflow() -> Graph:
    graph = Graph()
    
    # Define state type
    graph.add_node("intake", IntakeAgent)
    graph.add_node("transport", TransportAgent)
    graph.add_node("accommodation", AccommodationAgent)
    graph.add_node("experience", ExperienceAgent)
    graph.add_node("budget", BudgetAuditor)
    
    # Define edges
    graph.add_edge("intake", "transport")
    graph.add_edge("transport", "accommodation")
    graph.add_edge("accommodation", "experience")
    graph.add_edge("experience", "budget")
    graph.add_edge("budget", "intake")  # Conditional routing back to intake if budget exceeded
    
    return graph

if __name__ == "__main__":
    workflow = create_workflow()
    print("Workflow created successfully")