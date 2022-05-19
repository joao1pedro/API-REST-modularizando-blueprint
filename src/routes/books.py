from flask import Blueprint, jsonify, request

from ..extensions import db
from ..models.book import Book, BookSchema

api = Blueprint("api", __name__)


@api.route("/book", methods=["POST"])
def create_book():
    if request.method == "POST":
        data = request.get_json()

        book = Book(
            title=data.get("title"), author=data.get("author"), year=data.get("year")
        )
        db.session.add(book)
        db.session.commit()

        serializer = BookSchema()

        data = serializer.dump(book)

        return jsonify(data), 201


@api.route("/book/<string:title>", methods=["GET"])
def get_book_by_title(title):
    title = Book.query.filter_by(title=title).first()

    return {"title": title.title, "author": title.author}, 200


@api.route("/book", methods=["GET"])
def get_all_books():
    books = Book.query.all()
    serializer = BookSchema(many=True)
    data = serializer.dump(books)
    return jsonify(data), 200


@api.route("/book/<int:id>", methods=["PUT"])
def update_book(id):
    book = Book.get_by_id(id)

    data = request.get_json()

    book.title = data.get("title")
    book.author = data.get("author")
    book.year = data.get("year")

    db.session.commit()

    serializer = BookSchema()

    data = serializer.dump(book)

    return jsonify(data), 200


@api.route("/book/<int:id>", methods=["DELETE"])
def delete_book(id):
    data = Book.query.get(id)
    db.session.delete(data)
    db.session.commit()

    return jsonify({"message": "success"}), 204
