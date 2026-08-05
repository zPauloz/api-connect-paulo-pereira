from flask import Blueprint

from app.controllers.users_controller import (
    create_user,
    list_users,
    get_user,
    update_user,
    delete_user
)

users_bp = Blueprint("users", __name__)

users_bp.route("/users", methods=["POST"])(create_user)
users_bp.route("/users", methods=["GET"])(list_users)
users_bp.route("/users/<int:user_id>", methods=["GET"])(get_user)
users_bp.route("/users/<int:user_id>", methods=["PUT"])(update_user)
users_bp.route("/users/<int:user_id>", methods=["DELETE"])(delete_user)