import os
from dotenv import load_dotenv

load_dotenv()

class MockMCPServer:
    def __init__(self):
        self.flights = []
        self.hotels = []

    def search_flights(self, origin: str, destination: str, dates: str) -> list[Dict[str, Any]]:
        # Dummy data for flights
        return [
            {"name": "Flight A", "price": 150.0, "duration": "2h 30m"},
            {"name": "Flight B", "price": 200.0, "duration": "3h 15m"},
            {"name": "Flight C", "price": 250.0, "duration": "4h 00m"},
        ]

    def search_hotels(self, destination: str, dates: str, tier: str) -> list[Dict[str, Any]]:
        # Dummy data for hotels
        return [
            {"name": "Hotel X", "price": 80.0, "rating": 4.5, "tier": "budget"},
            {"name": "Hotel Y", "price": 120.0, "rating": 4.7, "tier": "mid-range"},
            {"name": "Hotel Z", "price": 180.0, "rating": 4.9, "tier": "mid-range"},
        ]

mcp_server = MockMCPServer()