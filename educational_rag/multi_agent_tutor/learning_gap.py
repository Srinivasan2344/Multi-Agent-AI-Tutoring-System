from student_history import student_history


def predict_learning_gaps():
    gaps = []

    for subject, scores in student_history.items():

        average_score = sum(scores) / len(scores)

        if average_score < 60:
            gaps.append(
                f"{subject.title()}: High learning gap detected."
            )

        elif average_score < 75:
            gaps.append(
                f"{subject.title()}: Moderate learning gap detected."
            )

        else:
            gaps.append(
                f"{subject.title()}: No significant learning gaps."
            )

    return gaps