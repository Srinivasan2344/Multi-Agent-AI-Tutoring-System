def validate_safety(response):

    unsafe_keywords = [
        "hack",
        "cheat",
        "violence",
        "harm",
        "illegal",
        "danger",
        "exploit",
        "abuse",
        "offensive",
        "inappropriate",
        "sensitive",
        "confidential",
        "private",
        "personal",
        "violent",
        "weapon",
        "drug",
        "terrorism",
        "extremism",
        "hate",

    ]

    violations = []

    response_lower = response.lower()

    for keyword in unsafe_keywords:

        if keyword in response_lower:
            violations.append(keyword)

    return violations