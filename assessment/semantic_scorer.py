from difflib import SequenceMatcher


def calculate_similarity(expected_answer, student_answer):
    similarity = SequenceMatcher(
        None,
        expected_answer.lower(),
        student_answer.lower()
    ).ratio()

    return round(similarity * 100, 2)