def evaluate_fairness(student_results):

    total_students = len(student_results)

    if total_students == 0:
        return {
            "fairness_score": 0,
            "status": "No data available."
        }

    recommended_count = 0

    for student in student_results:

        if student.get("recommended", False):
            recommended_count += 1

    fairness_score = (
        recommended_count / total_students
    ) * 100

    if fairness_score >= 70:
        status = "Fair"
    elif fairness_score >= 40:
        status = "Needs Review"
    else:
        status = "Potential Fairness Concern"

    return {
        "fairness_score": round(fairness_score, 2),
        "status": status
    }