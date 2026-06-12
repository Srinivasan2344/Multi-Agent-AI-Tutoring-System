from learning_gap import predict_learning_gaps

results = predict_learning_gaps()

print("\nLearning Gap Analysis:\n")

for result in results:
    print("-", result)