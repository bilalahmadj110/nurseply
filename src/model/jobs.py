from .abc import db, BaseModel


class Profile(db.Model, BaseModel):
    __tablename__ = 'profile'

    user_id = db.Column(db.Integer, db.ForeignKey('auth_user.id'), primary_key=True)
    # enum (US, CA)
    country = db.Column(db.String(2))
    zip_code = db.Column(db.String(10))
    profession = db.Column(db.String(50))

    primary_speciality = db.Column(db.String(50))
    experience = db.Column(db.Integer)

    primary_employment = db.Column(db.String(50))
    how_soon = db.Column(db.String(50))

    def __repr__(self):
        return '<Profile %r, %r, %r, %r, %r, %r, %r>' % (
        self.country, self.zip_code, self.profession, self.primary_speciality, self.experience, self.primary_employment,
        self.how_soon)
