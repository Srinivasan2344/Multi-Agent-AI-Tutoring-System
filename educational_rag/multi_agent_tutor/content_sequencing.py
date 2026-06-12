def recommend_learning_path(score):

    if score < 50:
        return [
            "1. Review Theory",
            "2. Watch Video Lessons",
            "3. Solve Basic Exercises",
            "4. Take Practice Quiz"
        ]

    elif score < 75:
        return [
            "1. Quick Theory Revision",
            "2. Solve Intermediate Problems",
            "3. Take Practice Quiz",
            "4. Review Mistakes"
        ]

    else:
        return [
            "1. Solve Advanced Problems",
            "2. Attempt Mock Tests",
            "3. Explore Real-world Applications",
            "4. Peer Teaching Activities"
        ]