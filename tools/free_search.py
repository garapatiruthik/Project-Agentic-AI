import duckduckgo_search

def search_reviews(query: str) -> str:
    """Search DuckDuckGo for reviews and return top result snippet."""
    results = duckduckgo_search DuckDuckGoSearchRun(query)
    return results[0] if results else "No reviews found"