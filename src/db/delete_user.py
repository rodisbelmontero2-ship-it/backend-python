from connection import get_connection


def delete_user(user_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM users WHERE id = %s",
        (user_id,)
    )

    deleted = cur.rowcount > 0

    conn.commit()
    cur.close()
    conn.close()

    if deleted:
        print(f"User {user_id} deleted successfully")
    else:
        print(f"User {user_id} not found")


if __name__ == "__main__":
    delete_user(3)  # ← puedes cambiar el ID