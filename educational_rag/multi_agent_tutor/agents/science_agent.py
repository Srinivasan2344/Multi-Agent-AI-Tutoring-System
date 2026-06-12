def handle_query(query):
    if "photosynthesis" in query:
        return """
Science Agent:
Photosynthesis is the process by which green plants use sunlight, carbon dioxide, and water to produce food.
"""
    
    return f"Science Agent: I can help with science topics related to '{query}'."