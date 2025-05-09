from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional
from src.etl import read_data_from_json_file
import json
import os


@dataclass
class Selectors:
    eps_list: str
    watch_buttons: str
    iframe: str
    referer: Optional[str] = r"https://m15.asd.rest/"


json_file_path = os.path.join(os.path.dirname(__file__), "selectors.json")

data = read_data_from_json_file(json_file_path)

selectors:Selectors = Selectors(**data["selectors"])