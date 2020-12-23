from app.app import db


class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String, nullable=False)
    avatar = db.Column(db.String, nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    residence_address = db.Column(db.String, nullable=False)
    phone = db.relationship('TelephoneModel', back_populates='user', cascade='all, delete-orphan')
    email_address = db.relationship('EmailAddressModel', back_populates='user', cascade='all, delete-orphan')


class TelephoneModel(db.Model):
    __tablename__ = 'telephone'
    id = db.Column(db.Integer, primary_key=True)
    phone_type = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('UserModel', back_populates='phone')


class EmailAddressModel(db.Model):
    __tablename__ = 'email_addr'
    id = db.Column(db.Integer, primary_key=True)
    mail_type = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('UserModel', back_populates='email_address')
