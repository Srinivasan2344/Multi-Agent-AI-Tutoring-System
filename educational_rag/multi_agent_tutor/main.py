from orchestrator import route_query
from memory import save_conversation, get_last_conversation

while True:
    query = input("\nAsk your question (type 'exit' to quit): ")

    if query.lower() == "exit":
        print("Thank you for using the Multi-Agent Tutoring System!")
        break

    previous = get_last_conversation()

    if previous:
        print(f"\nPrevious Query: {previous['query']}")

    response = route_query(query)

    print("\nResponse:")
    print(response)

    save_conversation(query, response)