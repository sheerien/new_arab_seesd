import json
from pathlib import Path
import re
from typing import Any, Optional

def read_data_from_json_file(filename: str) -> Optional[dict[str, Any]]:
    """
    Reads and parses a JSON file.

    Args:
        filename (str): Path to the JSON file.

    Returns:
        dict: Parsed JSON data, or None if file not found.
    """
    file_path = Path(filename)
    if not file_path.exists():
        print(f"Error: File '{filename}' not found.")
        return None

    with file_path.open(encoding="utf-8") as f:
        return json.load(f)


def save_to_json(data: list[dict[str, Any]], filename: str) -> None:
    """
    Saves a list of dictionaries to a JSON file.

    Args:
        data (list): Data to save.
        filename (str): Destination JSON file path.
    """
    file_path = Path(filename)
    with file_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"✅ JSON file saved: {file_path.resolve()}")

