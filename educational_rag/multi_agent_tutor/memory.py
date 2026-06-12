conversation_history = []

def save_conversation(query, response):
    conversation_history.append({
        "query": query,
        "response": response
    })

def get_last_conversation():
    if conversation_history:
        return conversation_history[-1]
    return None