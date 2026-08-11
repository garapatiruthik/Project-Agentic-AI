import os
from dotenv import load_dotenv
from typing import Dict, Any, List

load_dotenv()

class AccommodationAgent:
    def __init__(self, state: Dict[str, Any]):
        self.state = state
        self.mcp = __import__('tools.mcp_mock_server').mcp_server

    def run(self) -> Dict[str, Any]:
        tier = self.state["accommodation_tier"]
        options = self.mcp.search_hotels(
            self.state["destination"],
            self.state["dates"],
            tier
        )
        # Filter by tier and sort by price
        filtered = [opt for opt in options if opt["tier"] == tier]
        filtered.sort(key=lambda x: x["price"])
        self.state["accommodation_options"] = filtered[:3]  # Top 3 options
        self.state["current_step"] = "experience"
        return self.state