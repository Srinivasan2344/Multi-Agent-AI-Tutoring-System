from real_time_updates import update_recommendations

subject = input("Enter subject: ")
score = int(input("Enter latest score: "))

result = update_recommendations(subject, score)

print("\nUpdated Recommendation:")
print(result)