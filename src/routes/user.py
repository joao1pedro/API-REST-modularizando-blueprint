from flask import Blueprint, jsonify, request

from ..extensions import db
from ..models.user import User, UserSchema

main = Blueprint("main", __name__)


@main.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()

    user = User(name=data.get("name"))
    db.session.add(user)
    db.session.commit()

    serializer = UserSchema()

    data = serializer.dump(user)

    return jsonify(data), 201


@main.route("/user/<string:name>", methods=["GET"])
def get_user_name(name):
    user = User.query.filter_by(name=name).first()

    return {"name": user.name}, 200


@main.route("/user", methods=["GET"])
def get_all_user():
    user = User.query.all()
    serializer = UserSchema(many=True)
    data = serializer.dump(user)
    return jsonify(data), 200


@main.route("/user/<int:id>", methods=["PUT"])
def update_user(id):
    user = User.get_by_id(id)

    data = request.get_json()

    user.name = data.get("name")

    db.session.commit()

    serializer = UserSchema()

    data = serializer.dump(user)

    return jsonify(data), 200


@main.route("/user/<int:id>", methods=["DELETE"])
def delete_book(id):
    data = User.query.get(id)
    db.session.delete(data)
    db.session.commit()

    return jsonify({"message": "success"}), 204
