# storage.py

import json
import os

def load_data(filename: str):
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            if not isinstance(data, list):
                raise ValueError("Format data tidak valid (harus list)")
            return data
    except (json.JSONDecodeError, ValueError) as e:
        print(f"[ERROR] Gagal memuat data: {e}")
        return []

def save_data(filename: str, data: list):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"[ERROR] Gagal menyimpan data: {e}")
