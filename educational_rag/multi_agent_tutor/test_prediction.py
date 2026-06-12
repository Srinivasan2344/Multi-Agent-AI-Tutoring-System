from performance_prediction import predict_future_performance

results = predict_future_performance()

print("\nFuture Performance Prediction:\n")

for result in results:
    print("-", result)