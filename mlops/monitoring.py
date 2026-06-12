def monitor_model():

    metrics = {
        "accuracy": 89,
        "latency_ms": 120,
        "data_drift": False
    }

    return metrics


def check_model_health(metrics):

    alerts = []

    if metrics["accuracy"] < 85:
        alerts.append(
            "Accuracy dropped below acceptable threshold."
        )

    if metrics["latency_ms"] > 200:
        alerts.append(
            "Inference latency is too high."
        )

    if metrics["data_drift"]:
        alerts.append(
            "Potential data drift detected."
        )

    if not alerts:
        alerts.append(
            "Model is operating normally."
        )

    return alerts