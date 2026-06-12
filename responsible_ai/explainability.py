def generate_explanation(student_name, score, recommendation):

    explanation = f"""
Student: {student_name}

Reasoning:
- Current Performance Score: {score}%

Recommendation:
- {recommendation}

Explanation:
The recommendation was generated based on the student's
recent performance trends and learning analytics data.
Students with similar performance levels are encouraged
to follow the suggested intervention plan to improve outcomes.
"""

    return explanation.strip()