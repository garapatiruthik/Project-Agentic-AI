import os
from dotenv import load_dotenv
from typing import Dict, Any, List

load_dotenv()

class BudgetAuditor:
    def __init__(self, state: Dict[str, Any]):
        self.state = state

    def run(self) -> Dict[str, Any]:
        total_transport = sum(opt["price"] for opt in self.state["transport_options"])
        total_accommodation = sum(opt["price"] for opt in self.state["accommodation_options"])
        daily_expenses = sum(self.state["daily_expenses"])
        total_cost = total_transport + total_accommodation + (daily_expenses * 3)  # 3 days
        
        self.state["total_cost"] = total_cost
        self.state["current_step"] = "routing" if total_cost > self.state["max_budget"] else "complete"
        
        if total_cost > self.state["max_budget"]:
            # Route back to transport or accommodation to downgrade
            if self.state["transport_options"]:
                cheapest_transport = min(self.state["transport_options"], key=lambda x: x["price"])
                self.state["transport_options"] = [cheapest_transport]
            if self.state["accommodation_options"]:
                cheapest_accommodation = min(self.state["accommodation_options"], key=lambda x: x["price"])
                self.state["accommodation_options"] = [cheapest_accommodation]
                
        return self.state