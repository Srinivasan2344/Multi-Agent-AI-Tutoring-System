from student_history import student_history


def predict_future_performance():
    predictions = []

    for subject, scores in student_history.items():

        if len(scores) >= 2:
            improvement = scores[-1] - scores[-2]
            predicted_score = scores[-1] + improvement

            # Limit score between 0 and 100
            predicted_score = max(0, min(100, predicted_score))

            predictions.append(
                f"{subject.title()}: Predicted next score = {predicted_score}"
            )

    return predictions