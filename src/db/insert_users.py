from connection import get_connection


def insert_users():
    conn = get_connection()
    cur = conn.cursor()

    users = [
        ("Alice", "alice@email.com", 30),
        ("Bob", "bob@email.com", 25),
        ("Charlie", "charlie@email.com", 28),
    ]

    cur.executemany(
        "INSERT INTO users (name, email, age) VALUES (%s, %s, %s) "
        "ON CONFLICT (email) DO NOTHING;",
        users
    )

    conn.commit()
    cur.close()
    conn.close()
    print("Users inserted")


if __name__ == "__main__":
    insert_users()