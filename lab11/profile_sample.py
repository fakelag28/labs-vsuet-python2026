import json
from pathlib import Path

with open(Path(__file__).resolve().parent / "profile_sample.json", encoding="utf-8") as file:
    profile = json.load(file)
print(f"Учебные локальные данные: {profile['login']}")
