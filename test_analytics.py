from analytics.performance_analyzer import identify_low_performers
from analytics.dropout_predictor import predict_dropout_risk

print("\nLow Performing Students:\n")

low_performers = identify_low_performers()

for student in low_performers:
    print("-", student)


print("\nDropout Risk Analysis:\n")

dropout_risks = predict_dropout_risk()

for student in dropout_risks:
    print(
        f"- {student['name']} "
        f"(Risk Level: {student['risk_level']})"
    )

from analytics.engagement_scorer import calculate_engagement_scores


print("\nEngagement Scores:\n")

engagement_scores = calculate_engagement_scores()

for student in engagement_scores:
    print(
        f"- {student['name']}: "
        f"{student['engagement_score']}"
    )

from analytics.intervention_engine import generate_interventions


print("\nIntervention Recommendations:\n")

interventions = generate_interventions()

for student in interventions:

    print(f"\n{student['name']}:")

    for recommendation in student["recommendations"]:
        print(f"- {recommendation}")
        
from analytics.anomaly_detector import detect_anomalies


print("\nAnomaly Detection:\n")

anomalies = detect_anomalies()

if anomalies:

    for student in anomalies:

        print(f"\n{student['name']}:")

        for reason in student["reasons"]:
            print(f"- {reason}")

else:
    print("No anomalies detected.")