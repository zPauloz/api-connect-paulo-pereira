from flask import request, jsonify
from app.data.database import load_users, save_users, generate_id


def create_user():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON obrigatório"}), 400

    if not data.get("name"):
        return jsonify({"error": "Nome obrigatório"}), 400

    if not data.get("email"):
        return jsonify({"error": "Email obrigatório"}), 400

    users = load_users()

    user = {
        "id": generate_id(users),
        "name": data["name"],
        "email": data["email"]
    }

    users.append(user)
    save_users(users)

    return jsonify({"data": user}), 201


def list_users():
    return jsonify({"data": load_users()}), 200


def get_user(user_id):
    users = load_users()

    for user in users:
        if user["id"] == user_id:
            return jsonify({"data": user}), 200

    return jsonify({"error": "Usuário não encontrado"}), 404


def update_user(user_id):
    users = load_users()
    data = request.get_json()

    for i, user in enumerate(users):
        if user["id"] == user_id:
            users[i]["name"] = data["name"]
            users[i]["email"] = data["email"]

            save_users(users)

            return jsonify({"data": users[i]}), 200

    return jsonify({"error": "Usuário não encontrado"}), 404


def delete_user(user_id):
    users = load_users()

    for i, user in enumerate(users):
        if user["id"] == user_id:
            users.pop(i)
            save_users(users)

            return "", 204

    return jsonify({"error": "Usuário não encontrado"}), 404