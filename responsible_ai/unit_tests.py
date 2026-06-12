from responsible_ai.bias_detector import detect_bias
from responsible_ai.safety_validator import validate_safety


def run_unit_tests():

    test_results = []

    # Bias Detector Test
    bias_result = detect_bias(
        "All students struggle with mathematics."
    )

    test_results.append(
        {
            "test": "Bias Detection Test",
            "status": (
                "Passed"
                if "all students" in bias_result
                else "Failed"
            )
        }
    )

    # Safety Validator Test
    safety_result = validate_safety(
        "Students should not cheat in exams."
    )

    test_results.append(
        {
            "test": "Safety Validation Test",
            "status": (
                "Passed"
                if "cheat" in safety_result
                else "Failed"
            )
        }
    )

    return test_results