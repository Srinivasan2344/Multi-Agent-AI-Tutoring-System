def check_completeness(expected_answer, student_answer):

    expected_keywords = set(expected_answer.lower().split())
    student_keywords = set(student_answer.lower().split())

    matched_keywords = expected_keywords.intersection(student_keywords)

    completeness_score = (
        len(matched_keywords) / len(expected_keywords)
    ) * 100

    return round(completeness_score, 2)