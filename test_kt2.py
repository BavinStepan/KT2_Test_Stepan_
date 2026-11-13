import pytest
from string_utils import get_string_length
from file_saver import save_string_to_file


#Задание 1
@pytest.mark.parametrize("input_string, expected", [
    ("", 0),
    ("Привет", 6),
    ("   ", 3),
    ("Первая\nВторая", 13),
])
def test_string_length(input_string, expected):
    assert get_string_length(input_string) == expected


#Задание 2
def test_save_to_file(tmp_path):
    file_path = tmp_path / "output.txt"
    content = "Hello, pytest!"
    save_string_to_file(content, file_path)

    assert file_path.exists()
    assert file_path.read_text(encoding="utf-8") == content


#Задание 3
def test_insert_user(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
    db_connection.commit()
    cursor.execute("SELECT name FROM users")
    assert cursor.fetchone()[0] == "Alice"


def test_db_is_clean_for_next_test(db_connection):

    cursor = db_connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    assert cursor.fetchone()[0] == 0