from fine_tuning.evaluation import evaluate_models


def generate_comparison_report():

    results = evaluate_models()

    base = results["base_model"]
    fine_tuned = results["fine_tuned_model"]

    report = []

    for metric in base:

        improvement = fine_tuned[metric] - base[metric]

        report.append(
            {
                "metric": metric.capitalize(),
                "base_model": base[metric],
                "fine_tuned_model": fine_tuned[metric],
                "improvement": improvement
            }
        )

    return report