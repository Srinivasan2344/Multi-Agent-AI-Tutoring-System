from analytics.dashboard import generate_dashboard

dashboard = generate_dashboard()

print("\nLEARNING ANALYTICS DASHBOARD\n")

print("Low Performing Students:")
for student in dashboard["low_performers"]:
    print(f"- {student}")

print("\nDropout Risks:")
for student in dashboard["dropout_risks"]:
    print(
        f"- {student['name']} "
        f"({student['risk_level']} Risk)"
    )

print("\nEngagement Scores:")
for student in dashboard["engagement_scores"]:
    print(
        f"- {student['name']}: "
        f"{student['engagement_score']}"
    )

print("\nIntervention Recommendations:")
for student in dashboard["interventions"]:

    print(f"\n{student['name']}:")

    for recommendation in student["recommendations"]:
        print(f"  • {recommendation}")

print("\nAnomaly Detection:")

if dashboard["anomalies"]:

    for student in dashboard["anomalies"]:

        print(f"\n{student['name']}:")

        for reason in student["reasons"]:
            print(f"  • {reason}")

else:
    print("- No anomalies detected.")