experiments = []


def log_experiment(model_name, accuracy, parameters):

    experiment = {
        "model_name": model_name,
        "accuracy": accuracy,
        "parameters": parameters
    }

    experiments.append(experiment)

    return experiment


def get_experiments():

    return experiments