from responsible_ai.bias_detector import detect_bias
from responsible_ai.fairness_evaluator import evaluate_fairness
from responsible_ai.safety_validator import validate_safety

response = input("Enter AI response: ")

bias = detect_bias(response)

print("\nBias Detection Report:")

if bias:

    print("Potential bias indicators found:")

    for item in bias:
        print("-", item)

else:
    print("No obvious bias detected.")

sample_results = [
    {"name": "Student A", "recommended": True},
    {"name": "Student B", "recommended": True},
    {"name": "Student C", "recommended": False},
    {"name": "Student D", "recommended": True}
]

fairness_report = evaluate_fairness(
    sample_results
)

print("\nFairness Evaluation Report:")
print(
    f"Fairness Score: "
    f"{fairness_report['fairness_score']}%"
)

print(
    f"Status: "
    f"{fairness_report['status']}"
)

safety_response = input(
    "\nEnter response for safety validation: "
)

violations = validate_safety(
    safety_response
)

print("\nSafety Validation Report:")

if violations:

    print("Safety violations detected:")

    for violation in violations:
        print(f"- {violation}")

else:
    print("No safety violations detected.")

from responsible_ai.explainability import generate_explanation


print("\nExplainability Report:\n")

report = generate_explanation(
    "Student B",
    45,
    "Assign additional practice exercises."
)

print(report)

from responsible_ai.unit_tests import run_unit_tests


print("\nUnit Testing Report:\n")

results = run_unit_tests()

for result in results:

    print(
        f"{result['test']}: "
        f"{result['status']}"
    )

from responsible_ai.system_validation import (
    run_system_validation
)


print("\nEnd-to-End System Validation:\n")

validation_results = run_system_validation()

for result in validation_results:

    print(
        f"{result['component']}: "
        f"{result['status']}"
    )