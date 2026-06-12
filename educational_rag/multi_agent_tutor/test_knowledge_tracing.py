from knowledge_tracing import analyze_learning_trends

results = analyze_learning_trends()

print("\nLearning Trends:\n")

for result in results:
    print("-", result)