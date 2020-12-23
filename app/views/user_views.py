from flask_restful import Resource, reqparse, abort, fields, marshal_with
from flask_restful.inputs import date
import datetime


from app.models import UserModel, db

user_put_args = reqparse.RequestParser()
user_put_args.add_argument("fullname", type=str, help="Fullname", required=True)
user_put_args.add_argument("avatar", type=str, help="аватар", required=True)
user_put_args.add_argument("birth_date", type=date, help="формат даты должен быть yyyy-mm-dd", required=True)
user_put_args.add_argument("residence_address", type=str, help="Адресс проживания", required=True)

user_update_args = reqparse.RequestParser()
user_update_args.add_argument("fullname", type=str, help="Fullname")
user_update_args.add_argument("avatar", type=str, help="аватар")
user_update_args.add_argument("birth_date", type=date, help="формат даты должен быть yyyy-mm-dd")
user_update_args.add_argument("residence_address", type=str, help="Адресс проживания")

user_fields = {
    'id': fields.Integer,
    'fullname': fields.String,
    'avatar': fields.String,
    'birth_date': fields.String,
    'residence_address': fields.String
}


class User(Resource):
    @marshal_with(user_fields)
    def post(self, sort_field=None):
        user = UserModel.query.order_by(sort_field).all()

        return user

    @marshal_with(user_fields)
    def put(self):
        args = user_put_args.parse_args()
        if args['birth_date'] > datetime.datetime.now():
            abort(409, message="Дата рождения не может быть в будущем")
        user = UserModel(fullname=args['fullname'], avatar=args['avatar'], birth_date=args['birth_date'],
                         residence_address=args['residence_address'])

        if not user:
            abort(409, message="---------------")

        db.session.add(user)
        db.session.commit()

        return user, 201

    @marshal_with(user_fields)
    def patch(self, user_id):
        args = user_update_args.parse_args()
        user = UserModel.query.filter_by(id=user_id).first()
        if not user:
            abort(404, message="User doesn't exist, cannot update")

        if args['fullname']:
            user.fullname = args['fullname']
        if args['avatar']:
            user.avatar = args['avatar']
        if args['birth_date']:
            user.birth_date = args['birth_date']
        if args['residence_address']:
            user.residence_address = args['residence_address']

        db.session.commit()

        return user

    def delete(self, user_id):
        user = UserModel.query.filter(UserModel.id == user_id).first()

        if not user:
            abort(400, message={'No users with this id'})

        db.session.delete(user)
        db.session.commit()
        return '', 204
