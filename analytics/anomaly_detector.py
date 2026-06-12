from analytics.student_data import students


def detect_anomalies():

    anomalies = []

    for student in students:

        reasons = []

        if (
            student["attendance"] >= 80
            and student["score"] < 50
        ):
            reasons.append(
                "High attendance but low academic performance."
            )

        if (
            student["score"] >= 80
            and student["engagement"] < 50
        ):
            reasons.append(
                "Strong academic performance but low engagement."
            )

        if reasons:
            anomalies.append(
                {
                    "name": student["name"],
                    "reasons": reasons
                }
            )

    return anomalies