import os
from dotenv import load_dotenv
from langgraph import Graph, State
from state.graph_state import TravelState
from agents.intake_agent import IntakeAgent
from agents.transport_agent import TransportAgent
from agents.accommodation_agent import AccommodationAgent
from agents.experience_agent import ExperienceAgent
from agents.budget_auditor import BudgetAuditor

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
    graph.add_edge("budget", "intake")  # Loop back if budget exceeded
    
    return graph

if __name__ == "__main__":
    workflow = create_workflow()
    print("Workflow created successfully")