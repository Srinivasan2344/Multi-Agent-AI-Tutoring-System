from assessment.semantic_scorer import calculate_similarity
from assessment.rubric_evaluator import evaluate_rubric
from assessment.answer_completeness import check_completeness
from assessment.feedback_generator import generate_feedback
from assessment.plagiarism_checker import check_plagiarism


def assess_answer(expected_answer, student_answer):

    similarity_score = calculate_similarity(
        expected_answer,
        student_answer
    )

    rubric_result = evaluate_rubric(similarity_score)

    completeness_score = check_completeness(
        expected_answer,
        student_answer
    )

    feedback = generate_feedback(
        similarity_score,
        completeness_score
    )

    plagiarism_score, plagiarism_status = check_plagiarism(
        expected_answer,
        student_answer
    )

    return {
        "similarity_score": similarity_score,
        "completeness_score": completeness_score,
        "marks": rubric_result["marks"],
        "performance": rubric_result["performance"],
        "feedback": feedback,
        "plagiarism_score": plagiarism_score,
        "plagiarism_status": plagiarism_status
    }