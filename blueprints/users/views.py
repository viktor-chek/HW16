from flask import Blueprint, jsonify, render_template, request, json
from models import User
from database import Database

users_blueprint = Blueprint("users_blueprint", __name__)


@users_blueprint.route("/")
def main_page():
    return render_template('main.html')


@users_blueprint.route("/users", methods=['GET', 'POST'])
def page_users():
    if request.method == 'GET':
        users = []
        for item in User.query.all():
            users.append(item.create_dict())
        return jsonify(users)
    elif request.method == 'POST':
        user_info = json.loads(request.data)
        Database().add_user(user_info)
        return ""


@users_blueprint.route("/users/<int:pk>", methods=['GET', 'PUT', 'DELETE'])
def page_user_by_id(pk):
    if request.method == 'GET':
        user = User.query.get(pk)
        result = User.create_dict(user)
        return jsonify(result)
    elif request.method == 'PUT':
        user_info = json.loads(request.data)
        Database().update_user(user_info, pk)
        return ""
    elif request.method == 'DELETE':
        Database().delete_user(pk)
        return ""
