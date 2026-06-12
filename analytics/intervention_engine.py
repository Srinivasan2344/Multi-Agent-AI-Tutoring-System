from analytics.student_data import students


def generate_interventions():

    recommendations = []

    for student in students:

        actions = []

        if student["score"] < 50:
            actions.append(
                "Assign additional practice exercises."
            )

        if student["attendance"] < 70:
            actions.append(
                "Schedule academic counseling sessions."
            )

        if student["engagement"] < 60:
            actions.append(
                "Provide interactive learning activities."
            )

        if actions:
            recommendations.append(
                {
                    "name": student["name"],
                    "recommendations": actions
                }
            )

    return recommendations