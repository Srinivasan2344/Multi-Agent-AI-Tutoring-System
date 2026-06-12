from responsible_ai.bias_detector import detect_bias
from responsible_ai.safety_validator import validate_safety
from responsible_ai.fairness_evaluator import evaluate_fairness
from responsible_ai.explainability import generate_explanation


def run_system_validation():

    results = []

    # Bias Validation
    bias_result = detect_bias(
        "All students need additional practice."
    )

    results.append(
        {
            "component": "Bias Detection",
            "status": (
                "Passed"
                if "all students" in bias_result
                else "Failed"
            )
        }
    )

    # Safety Validation
    safety_result = validate_safety(
        "Students should not cheat in exams."
    )

    results.append(
        {
            "component": "Safety Validation",
            "status": (
                "Passed"
                if "cheat" in safety_result
                else "Failed"
            )
        }
    )

    # Fairness Evaluation
    fairness_result = evaluate_fairness(
        [
            {"recommended": True},
            {"recommended": True},
            {"recommended": False},
            {"recommended": True}
        ]
    )

    results.append(
        {
            "component": "Fairness Evaluation",
            "status": (
                "Passed"
                if fairness_result["fairness_score"] >= 70
                else "Failed"
            )
        }
    )

    # Explainability
    explanation = generate_explanation(
        "Student A",
        85,
        "Continue regular revision."
    )

    results.append(
        {
            "component": "Explainability",
            "status": (
                "Passed"
                if "Student A" in explanation
                else "Failed"
            )
        }
    )

    return results