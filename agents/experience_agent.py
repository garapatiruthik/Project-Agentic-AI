import os
from dotenv import load_dotenv
from typing import Dict, Any, List

load_dotenv()

class ExperienceAgent:
    def __init__(self, state: Dict[str, Any]):
        self.state = state

    def run(self) -> Dict[str, Any]:
        interests = self.state["interests"]
        activities = []
        for interest in interests:
            if interest == "history":
                activities.append("Visit historic taverns")
            elif interest == "pubs":
                activities.append("Explore local pubs and breweries")
            elif interest == "foodie":
                activities.append("Discover street food hubs")
        self.state["daily_expenses"] = [50.0] * len(activities)  # Dummy daily expense
        self.state["current_step"] = "budget"
        return self.state