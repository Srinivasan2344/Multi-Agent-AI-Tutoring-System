from fine_tuning.preprocessor import preprocess_data
from fine_tuning.prompt_engineering import create_prompt
from fine_tuning.fine_tuner import simulate_fine_tuning
from fine_tuning.evaluation import evaluate_models
from fine_tuning.comparison_report import generate_comparison_report

data = preprocess_data()

print("\nProcessed Dataset:\n")

for sample in data:

    print("Question:", sample["input"])
    print("Answer:", sample["output"])
    print("-" * 40)

print("\nPrompt Engineering Examples:\n")

questions = [
    "What is photosynthesis?",
    "Explain machine learning.",
    "Define algebra."
]

for question in questions:

    prompt = create_prompt(question)

    print(prompt)
    print("\n" + "=" * 50 + "\n")

from fine_tuning.fine_tuner import simulate_fine_tuning


result = simulate_fine_tuning()

print("\nFine-Tuning Summary:")
print(f"Samples Used: {result['samples_used']}")
print(f"Status: {result['status']}")
print(f"Model Version: {result['model_version']}")

from fine_tuning.evaluation import evaluate_models


results = evaluate_models()

print("\nModel Evaluation Results")
print("=" * 40)

print("\nBase Model:")
for metric, value in results["base_model"].items():
    print(f"{metric.capitalize()}: {value}%")

print("\nFine-Tuned Model:")
for metric, value in results["fine_tuned_model"].items():
    print(f"{metric.capitalize()}: {value}%")


comparison = generate_comparison_report()

print("\nBase Model vs Fine-Tuned Model")
print("=" * 50)

for item in comparison:

    print(f"\nMetric: {item['metric']}")
    print(f"Base Model       : {item['base_model']}%")
    print(f"Fine-Tuned Model : {item['fine_tuned_model']}%")
    print(f"Improvement      : +{item['improvement']}%")