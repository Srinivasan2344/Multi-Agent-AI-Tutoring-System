from .agents.math_agent import handle_query as math_agent
from .agents.science_agent import handle_query as science_agent
from .agents.programming_agent import handle_query as programming_agent
from .agents.language_agent import handle_query as language_agent

from .retriever import retrieve_context
from .semantic_retriever import semantic_search


def route_query(query):
    query = query.lower()

    # Multi-Agent Collaboration + Semantic Search
    if "machine learning" in query:
        results = semantic_search(query)

        retrieved_context = "\n\n".join(
            [doc.page_content for doc in results]
        )

        math_response = math_agent(query)
        programming_response = programming_agent(query)

        return f"""
Primary Agents: Math Agent + Programming Agent
Confidence Score: 95%

Retrieved Context:
{retrieved_context}

Collaborative Response:

{math_response}

{programming_response}
"""

    # Confidence scores
    scores = {
        "programming": 0,
        "math": 0,
        "science": 0,
        "language": 0
    }

    # Keywords
    programming_keywords = [
        "python",
        "java",
        "programming",
        "code",
        "loop",
        "function",
        "algorithm"
    ]

    math_keywords = [
        "math",
        "algebra",
        "equation",
        "calculus",
        "geometry"
    ]

    science_keywords = [
        "science",
        "physics",
        "chemistry",
        "biology",
        "photosynthesis"
    ]

    # Calculate confidence scores
    for keyword in programming_keywords:
        if keyword in query:
            scores["programming"] += 60

    for keyword in math_keywords:
        if keyword in query:
            scores["math"] += 60

    for keyword in science_keywords:
        if keyword in query:
            scores["science"] += 60

    # Find best agent
    best_agent = max(scores, key=scores.get)
    confidence = scores[best_agent]

    # Fallback mechanism
    if confidence < 50:
        response = language_agent(query)

        return f"""
Fallback Agent Activated
Confidence Score: {confidence}%

{response}
"""

    # Retrieve context from PDF
    context = retrieve_context(query)

    # Route query
    if best_agent == "programming":
        response = programming_agent(query)

    elif best_agent == "math":
        response = math_agent(query)

    elif best_agent == "science":
        response = science_agent(query)

    else:
        response = language_agent(query)

    return f"""
Primary Agent: {best_agent.title()} Agent
Confidence Score: {confidence}%

Retrieved Context:
{context}

Agent Response:
{response}
"""