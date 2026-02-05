import psycopg2
from psycopg2.extensions import connection


def get_connection() -> connection:
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="backend_db",
        user="postgres",
        password="Rodi***"
    )