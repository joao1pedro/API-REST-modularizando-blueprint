from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

db = SQLAlchemy()
migrate = Migrate()
