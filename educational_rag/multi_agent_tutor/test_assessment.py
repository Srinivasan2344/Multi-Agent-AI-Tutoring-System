import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from assessment.assessment_orchestrator import assess_answer

expected = input("Enter expected answer: ")
student = input("Enter student answer: ")

result = assess_answer(expected, student)

print("\nAssessment Report")
print("-" * 40)

print(f"Similarity Score: {result['similarity_score']}%")
print(f"Completeness Score: {result['completeness_score']}%")
print(f"Marks Awarded: {result['marks']}/10")
print(f"Performance: {result['performance']}")

print("\nFeedback:")
for item in result["feedback"]:
    print(f"- {item}")

print("\nPlagiarism Check:")
print(f"Plagiarism Score: {result['plagiarism_score']}%")
print(f"Status: {result['plagiarism_status']}")