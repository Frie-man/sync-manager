from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

from .database import db


class User(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    role = db.Column(db.String(32), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow())
    updated = db.Column(db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())

    @property
    def password(self):
        raise AttributeError('Not allowed')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def user_by_username(_username):
        return User.query.filter_by(username=_username).first()

    @staticmethod
    def add_user(_username, _role, _password):
        _id = uuid.uuid4()
        new_user = User(id=_id, username=_username, role=_role, password=_password)
        db.session.add(new_user)
        db.session.commit()

    @staticmethod
    def has_role(username, role):
        user = User.user_by_username(username)
        if not user:
            return False
        if user.role == role:
            return True
        return False

    def __repr__(self):
        return '<User %r>' % self.username
