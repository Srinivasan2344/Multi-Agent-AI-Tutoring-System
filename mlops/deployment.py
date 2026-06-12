deployed_models = []


def deploy_model(model_name, version):

    deployment = {
        "model_name": model_name,
        "version": version,
        "status": "Deployed"
    }

    deployed_models.append(deployment)

    return deployment


def get_deployments():

    return deployed_models