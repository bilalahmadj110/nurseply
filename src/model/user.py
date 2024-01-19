from werkzeug.security import generate_password_hash, check_password_hash
import enum

from .abc import db, BaseModel

class SignInProvider(enum.Enum):
    GOOGLE = 'google'
    FACEBOOK = 'facebook'
    TWITTER = 'twitter'
    LINKEDIN = 'linkedin'
    EMAIL = 'email'


class User(db.Model, BaseModel):
    __tablename__ = 'auth_user'

    # uuid
    id = db.Column(db.Integer, primary_key=True)
    profile = db.relationship('Profile', uselist=False, backref='auth_user')

    first_name = db.Column(db.String(70), nullable=False)
    last_name = db.Column(db.String(70), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120), nullable=True)
    sign_in_provider = db.Column(db.Enum(SignInProvider), default=SignInProvider.EMAIL)
    is_email_verified = db.Column(db.Boolean, default=False)



    is_active = db.Column(db.Boolean, default=True)
    is_admin = db.Column(db.Boolean, default=False)


    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def __init__(self, email=None, password=None):
        if email:
            self.email = email.lower()
        if password:
            self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User %r>' % self.email
