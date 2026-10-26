
import psycopg
from config import DATABASE_URL


def get_connection():
    return psycopg.connect(DATABASE_URL)


if __name__ == "__main__":
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT current_database(), current_user;"
                )
                database, user = cur.fetchone()

                print("Connection successful!")
                print(f"Database: {database}")
                print(f"User: {user}")

    except Exception as exc:
        print(f"Connection failed: {exc}")
