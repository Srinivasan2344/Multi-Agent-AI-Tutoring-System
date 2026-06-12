def evaluate_models():

    base_model = {
        "accuracy": 72,
        "relevance": 70,
        "clarity": 75
    }

    fine_tuned_model = {
        "accuracy": 88,
        "relevance": 90,
        "clarity": 87
    }

    return {
        "base_model": base_model,
        "fine_tuned_model": fine_tuned_model
    }