def generate_feedback(similarity_score, completeness_score):

    feedback = []

    if similarity_score >= 80:
        feedback.append("Excellent understanding of the concept.")
    elif similarity_score >= 60:
        feedback.append("Good understanding, but there is room for improvement.")
    else:
        feedback.append("Revise the topic and improve conceptual clarity.")

    if completeness_score >= 80:
        feedback.append("Most key points were covered in the answer.")
    elif completeness_score >= 60:
        feedback.append("Some important points are missing.")
    else:
        feedback.append("The answer lacks several important concepts.")

    return feedback