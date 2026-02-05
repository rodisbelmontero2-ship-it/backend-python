from services.statistics import process_users


if __name__ == "__main__":
    users_data = [
        {"name": "Alice", "score": 85.0},
        {"name": "Bob", "score": 92.0},
        {"name": "Charlie", "score": 72.0},
    ]

    average_score = process_users(users_data)
    print(f"Average score: {average_score:.2f}")