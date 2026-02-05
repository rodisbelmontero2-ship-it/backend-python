from typing import List, Dict


def calculate_average(values: List[float]) -> float:
    if not values:
        raise ValueError("The list is empty")

    return sum(values) / len(values)


def process_users(users: List[Dict[str, float]]) -> float:
    scores = [user["score"] for user in users]
    return calculate_average(scores)