import os
from dotenv import load_dotenv
from langchain_groq import Groq
from typing import Dict, Any, List

load_dotenv()

class TransportAgent:
    def __init__(self, state: Dict[str, Any]):
        self.state = state
        self.mcp = __import__('tools.mcp_mock_server').mcp_server

    def run(self) -> Dict[str, Any]:
        options = self.mcp.search_flights(
            self.state["origin"],
            self.state["destination"],
            self.state["dates"]
        )
        self.state["transport_options"] = options[:3]  # Top 3 options
        self.state["current_step"] = "accommodation"
        return self.state