from student_history import student_history


def analyze_learning_trends():
    trends = []

    for subject, scores in student_history.items():

        if scores[-1] > scores[0]:
            trends.append(
                f"{subject.title()}: Performance is improving."
            )

        elif scores[-1] < scores[0]:
            trends.append(
                f"{subject.title()}: Performance is declining."
            )

        else:
            trends.append(
                f"{subject.title()}: Performance is stable."
            )

    return trends