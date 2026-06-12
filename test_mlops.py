from mlops.experiment_tracker import (
    log_experiment,
    get_experiments
)

log_experiment(
    "educational-llm-v1",
    88,
    {
        "learning_rate": 0.001,
        "epochs": 5
    }
)

log_experiment(
    "educational-llm-v2",
    91,
    {
        "learning_rate": 0.0005,
        "epochs": 10
    }
)

print("\nExperiment Tracking Dashboard:\n")

for experiment in get_experiments():

    print(
        f"Model: {experiment['model_name']}"
    )

    print(
        f"Accuracy: {experiment['accuracy']}%"
    )

    print(
        f"Parameters: {experiment['parameters']}"
    )

    print("-" * 40)

from mlops.model_registry import (
    register_model,
    get_registered_models
)


register_model(
    "educational-llm",
    "v1.0",
    "Production"
)

register_model(
    "educational-llm",
    "v2.0",
    "Staging"
)


print("\nModel Registry:\n")

for model in get_registered_models():

    print(
        f"Model: {model['model_name']}"
    )

    print(
        f"Version: {model['version']}"
    )

    print(
        f"Status: {model['status']}"
    )

    print("-" * 40)

from mlops.deployment import (
    deploy_model,
    get_deployments
)


deploy_model(
    "educational-llm",
    "v1.0"
)

print("\nDeployment Dashboard:\n")

for deployment in get_deployments():

    print(
        f"Model: {deployment['model_name']}"
    )

    print(
        f"Version: {deployment['version']}"
    )

    print(
        f"Status: {deployment['status']}"
    )

    print("-" * 40)

from mlops.retraining_pipeline import (
    check_retraining_need,
    retrain_model
)


print("\nRetraining Pipeline:\n")

result = check_retraining_need(82)

print(result["message"])

if result["retraining_required"]:

    retraining_result = retrain_model()

    print(
        f"\nRetraining Status: "
        f"{retraining_result['status']}"
    )

    print(
        f"New Model Version: "
        f"{retraining_result['new_model_version']}"
    )

from mlops.monitoring import (
    monitor_model,
    check_model_health
)


print("\nModel Monitoring Dashboard:\n")

metrics = monitor_model()

print(f"Accuracy: {metrics['accuracy']}%")
print(f"Latency: {metrics['latency_ms']} ms")
print(f"Data Drift: {metrics['data_drift']}")

print("\nHealth Status:")

alerts = check_model_health(metrics)

for alert in alerts:
    print(f"- {alert}")

from mlops.cicd_pipeline import run_cicd_pipeline


print("\nCI/CD Pipeline Simulation:\n")

pipeline_result = run_cicd_pipeline()

for step in pipeline_result["steps"]:
    print(f"✓ {step}")

print(
    f"\nPipeline Status: "
    f"{pipeline_result['status']}"
)