from connection import get_connection


def test():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT current_database(), version();")
    db, version = cur.fetchone()
    print("Connected to:", db)
    print("PostgreSQL:", version)
    cur.close()
    conn.close()


if __name__ == "__main__":
    test()