# Утилиталар кейін қосылады
import json
import os


USERS_FILE = "users.json"

def save_users(users):
    with open("users.json", "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)

def load_users():
    try:
        with open("users.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {}

def get_top_10(users):
    # Пайдаланушыларды ұпайы бойынша кері тәртіпте сұрыптау
    sorted_users = sorted(users.items(), key=lambda x: x[1].get("score", 0), reverse=True)
    return sorted_users[:10]
# utils.py
# utils.py

def get_top_10(users):
    sorted_users = sorted(users.items(), key=lambda x: x[1].get('score', 0), reverse=True)
    top_10 = sorted_users[:10]
    return top_10


def give_superbaxa_status(user_id, users):
    if user_id not in users:
        users[user_id] = {}
    users[user_id]['superbaxa'] = True
    users[user_id]['score'] = 10000  # Немесе сен қалаған үлкен сан
    save_users(users)

def load_users():
    try:
        with open("users.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open("users.json", "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)
