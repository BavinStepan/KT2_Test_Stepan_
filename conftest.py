import sqlite3
import pytest


@pytest.fixture
def db_connection(tmp_path):

    db_file = tmp_path / "test.db"
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    """)
    conn.commit()

    yield conn

    conn.close()