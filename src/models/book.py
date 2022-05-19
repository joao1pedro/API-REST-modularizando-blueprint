from ..extensions import Schema, db, fields


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)


class BookSchema(Schema):
    id = fields.Integer()
    title = fields.String()
    author = fields.String()
    year = fields.Integer()
