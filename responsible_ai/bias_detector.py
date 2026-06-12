def detect_bias(response):

    biased_terms = [
        "always",
        "never",
        "all students",
        "only",
        "best",
        "worst",
        "everyone",
        "nobody",
        "must",
        "should",
        "can't",
        "impossible",
        "guaranteed",
        "worst case",
        "best case",
        "perfect",
        "flawless",
        "terrible",
        "amazing",
        "incredible",
        "disaster",
        "miracle",
        "unfair",
        "biased",
        "prejudice",
        "stereotype",
        "discrimination",
        "inequality",
        "privilege",
        "oppression",
        "marginalization",
        "exclusion",
        "dominance",
        "subordination",
        "superiority",
        "inferiority",
        "victim",
        "perpetrator",
        "oppressor",
        "resistor",
        "ally",
        "advocate",
        "champion",
        "defender",
        "opponent",
        "critic",
        "supporter",
        "proponent",
        "detractor",
        "extreme",
        "radical",
        "moderate",
        "conservative",
        "liberal",
        "progressive",
        "traditional",
        "modern",
        "outdated",
        "innovative",
        "effective",
        "ineffective",
        "successful",
        "unsuccessful",
        "efficient",
        "inefficient",
        "productive",
        "unproductive",
        "valuable",
        "worthless"
    ]

    detected_bias = []

    response_lower = response.lower()

    for term in biased_terms:

        if term in response_lower:
            detected_bias.append(term)

    return detected_bias