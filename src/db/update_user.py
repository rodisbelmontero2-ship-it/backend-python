from connection import get_connection


def update_user_email(user_id: int, new_email: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "UPDATE users SET email = %s WHERE id = %s;",
        (new_email, user_id)
    )

    conn.commit()
    updated = cur.rowcount
    cur.close()
    conn.close()

    if updated:
        print(f"User {user_id} updated successfully")
    else:
        print(f"User {user_id} not found")


if __name__ == "__main__":
    update_user_email(1, "alice.new@email.com")