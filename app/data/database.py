import json
import os

DATABASE_FILE = "app/data/users.json"


def load_users():
    if not os.path.exists(DATABASE_FILE):
        return []

    with open(DATABASE_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_users(users):
    with open(DATABASE_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4, ensure_ascii=False)


def generate_id(users):
    if not users:
        return 1

    return max(user["id"] for user in users) + 1