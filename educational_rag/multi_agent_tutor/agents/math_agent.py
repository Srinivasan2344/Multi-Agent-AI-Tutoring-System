def handle_query(query):
    if "machine learning" in query:
        return """
Math Agent:
Machine Learning relies on concepts such as:
- Linear Algebra
- Probability
- Statistics
- Optimization
"""
    
    return f"Math Agent: I can help with mathematical concepts related to '{query}'."