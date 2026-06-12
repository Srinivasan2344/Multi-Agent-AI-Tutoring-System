from semantic_retriever import semantic_search

query = input("Enter your question: ")

results = semantic_search(query)

print("\nTop Relevant Chunks:\n")

for i, doc in enumerate(results, 1):
    print(f"Chunk {i}:")
    print(doc.page_content)
    print("-" * 500)