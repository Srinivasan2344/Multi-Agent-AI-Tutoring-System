from fine_tuning.preprocessor import preprocess_data


def simulate_fine_tuning():

    data = preprocess_data()

    print("\nStarting Fine-Tuning Simulation...\n")

    for index, sample in enumerate(data, start=1):

        print(f"Training Sample {index}")
        print(f"Input : {sample['input']}")
        print(f"Output: {sample['output']}")
        print("-" * 50)

    print("\nFine-Tuning Simulation Completed Successfully!")

    return {
        "samples_used": len(data),
        "status": "Completed",
        "model_version": "educational-llm-v1"
    }