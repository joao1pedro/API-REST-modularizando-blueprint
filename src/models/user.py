from ..extensions import Schema, db, fields


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)


class UserSchema(Schema):
    id = fields.Integer()
    name = fields.String()
