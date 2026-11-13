from pathlib import Path

def save_string_to_file(text: str, file_path: Path) -> None:
    file_path.write_text(text, encoding="utf-8")