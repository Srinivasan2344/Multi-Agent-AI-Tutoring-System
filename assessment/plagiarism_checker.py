from difflib import SequenceMatcher


def check_plagiarism(expected_answer, student_answer):

    similarity = SequenceMatcher(
        None,
        expected_answer.lower(),
        student_answer.lower()
    ).ratio()

    plagiarism_score = round(similarity * 100, 2)

    if plagiarism_score >= 90:
        status = "High plagiarism detected."
    elif plagiarism_score >= 70:
        status = "Moderate plagiarism detected."
    else:
        status = "No significant plagiarism detected."

    return plagiarism_score, status