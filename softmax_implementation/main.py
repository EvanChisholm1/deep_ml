import math

def softmax(scores: list[float]) -> list[float]:
    denominator = sum([math.exp(i) for i in scores])

    probabilities = [math.exp(i) / denominator for i in scores]

    return probabilities
