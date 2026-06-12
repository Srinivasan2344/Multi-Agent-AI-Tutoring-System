from student_data import student_performance


def update_recommendations(subject, new_score):
    student_performance[subject.lower()] = new_score

    if new_score < 50:
        return f"{subject.title()}: High Priority - Immediate attention required."

    elif new_score < 75:
        return f"{subject.title()}: Medium Priority - Continue practicing regularly."

    else:
        return f"{subject.title()}: Low Priority - Maintain current performance."