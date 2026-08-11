import os
from dotenv import load_dotenv
from langchain_groq import Groq
from langchain.schema import AgentState
from typing import Dict, Any, List

load_dotenv()

class IntakeAgent:
    def __init__(self, state: Dict[str, Any]):
        self.state = state

    def run(self) -> Dict[str, Any]:
        # Parse structured parameters from user input
        self.state["interests"] = self.state.get("interests", [])
        self.state["accommodation_tier"] = self.state.get("accommodation_tier", "budget")
        self.state["current_step"] = "transport"
        return self.state