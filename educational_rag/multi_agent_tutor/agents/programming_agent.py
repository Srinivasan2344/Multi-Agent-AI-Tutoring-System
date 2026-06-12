def handle_query(query):
    if "machine learning" in query:
        return """
Programming Agent:
Machine Learning algorithms can be implemented using Python libraries such as:
- NumPy
- Pandas
- Scikit-learn
- TensorFlow
- PyTorch
"""
    
    return f"Programming Agent: I can help with programming topics related to '{query}'."