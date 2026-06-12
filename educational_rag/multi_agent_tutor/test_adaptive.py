from adaptive_engine import generate_study_plan

plan = generate_study_plan()

print("\nPersonalized Study Plan:\n")

for item in plan:
    print("-", item)