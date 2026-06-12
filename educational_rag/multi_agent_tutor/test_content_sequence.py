from content_sequencing import recommend_learning_path

score = int(input("Enter student score: "))

path = recommend_learning_path(score)

print("\nRecommended Learning Sequence:\n")

for step in path:
    print(step)