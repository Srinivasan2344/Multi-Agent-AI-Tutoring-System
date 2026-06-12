from fine_tuning.dataset import training_data

def preprocess_data():

    processed_data = []

    for item in training_data:

        processed_data.append(
            {
                "input": item["question"].strip(),
                "output": item["answer"].strip()
            }
        )

    return processed_data