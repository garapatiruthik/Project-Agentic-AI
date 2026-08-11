from typing import TypedDict, Dict, Any

class TravelState(Dict[str, Any]):
    origin: str
    destination: str
    dates: str
    max_budget: float
    interests: list[str]
    accommodation_tier: str
    transport_options: list[Dict[str, Any]] = []
    accommodation_options: list[Dict[str, Any]] = []
    daily_expenses: list[float] = []
    total_cost: float = 0.0
    current_step: str = "intake"