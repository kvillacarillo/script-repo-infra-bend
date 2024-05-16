

import os
import psycopg2

def add_database_credentials(host, port, user, password, dbname):
    """
    Add database credentials.

    Args:
        host (str): The host of the database.
        port (int): The port of the database.
        user (str): The user for the database credentials.
        password (str): The password for the database credentials.
        dbname (str): The name of the database.

    """
    connection_string = f"host={host} port={port} user=postgres password={os.environ['POSTGRES_PASSWORD']}"

    try:
        with psycopg2.connect(connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    CREATE USER IF NOT EXISTS %s WITH PASSWORD %s;
                    GRANT ALL PRIVILEGES ON DATABASE %s TO %s;
                    """,
                    (user, password, dbname, user)
                )
                conn.commit()
    except psycopg2.Error as e:
        print(f"Error adding database credentials: {e}")