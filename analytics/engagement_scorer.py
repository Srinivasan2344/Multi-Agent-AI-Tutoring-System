from analytics.student_data import students


def calculate_engagement_scores():

    engagement_results = []

    for student in students:

        score = (
            student["attendance"] * 0.4 +
            student["engagement"] * 0.6
        )

        engagement_results.append(
            {
                "name": student["name"],
                "engagement_score": round(score, 2)
            }
        )

    return engagement_results