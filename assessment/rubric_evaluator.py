def evaluate_rubric(score):

    if score >= 80:
        return {
            "marks": 10,
            "performance": "Excellent"
        }

    elif score >= 60:
        return {
            "marks": 7,
            "performance": "Good"
        }

    elif score >= 40:
        return {
            "marks": 5,
            "performance": "Average"
        }

    else:
        return {
            "marks": 2,
            "performance": "Needs Improvement"
        }