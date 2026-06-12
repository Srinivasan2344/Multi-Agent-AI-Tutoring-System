registered_models = []


def register_model(model_name, version, status):

    model = {
        "model_name": model_name,
        "version": version,
        "status": status
    }

    registered_models.append(model)

    return model


def get_registered_models():

    return registered_models