from student_data import student_performance


def generate_study_plan():
    recommendations = []

    for subject, score in student_performance.items():

        if score < 50:
            recommendations.append(
                f"High Priority: Spend extra time improving {subject.title()}."
            )

        elif score < 75:
            recommendations.append(
                f"Medium Priority: Practice more exercises in {subject.title()}."
            )

        else:
            recommendations.append(
                f"Low Priority: Continue regular revision in {subject.title()}."
            )

    return recommendations