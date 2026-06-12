from analytics.student_data import students


def predict_dropout_risk():

    at_risk_students = []

    for student in students:

        if (
            student["attendance"] < 70
            and student["score"] < 50
        ):

            at_risk_students.append(
                {
                    "name": student["name"],
                    "risk_level": "High"
                }
            )

        elif (
            student["attendance"] < 80
            or student["score"] < 60
        ):

            at_risk_students.append(
                {
                    "name": student["name"],
                    "risk_level": "Medium"
                }
            )

    return at_risk_students