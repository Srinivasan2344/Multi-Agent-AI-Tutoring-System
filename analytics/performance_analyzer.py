from analytics.student_data import students


def identify_low_performers():

    low_performers = []

    for student in students:
        if student["score"] < 50:
            low_performers.append(student["name"])

    return low_performers