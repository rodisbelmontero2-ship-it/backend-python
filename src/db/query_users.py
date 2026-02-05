from connection import get_connection


def get_users():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name, email, age FROM users;")
    users = cur.fetchall()

    for user in users:
        print(user)

    cur.close()
    conn.close()


if __name__ == "__main__":
    get_users()