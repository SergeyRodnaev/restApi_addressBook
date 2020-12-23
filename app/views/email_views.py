from flask_restful import Resource, reqparse, abort, fields, marshal_with
from app.models import db, EmailAddressModel

email_put_args = reqparse.RequestParser()
email_put_args.add_argument("mail_type", type=str, choices=('Личная', 'Рабочая'),
                            help="Почта может быть только личная или рабочая", required=True)
email_put_args.add_argument("email", type=str, help="Почта должна содержать @", required=True)
email_put_args.add_argument("user_id", type=int, help="id пользователя почты", required=True)

email_update_args = reqparse.RequestParser()
email_update_args.add_argument("mail_type", type=str, choices=('Личная', 'Рабочая'),
                               help="Почта может быть только личная или рабочая")
email_update_args.add_argument("email", type=str, help="Почта должна содержать @")

email_address_fields = {
    'id': fields.Integer,
    'mail_type': fields.String,
    'email': fields.String,
    'user_id': fields.Integer
}


class EmailAddress(Resource):
    @marshal_with(email_address_fields)
    def post(self, sort_field=None):
        email = EmailAddressModel.query.order_by(sort_field).all()

        return email

    @marshal_with(email_address_fields)
    def put(self):
        args = email_put_args.parse_args()

        email = EmailAddressModel(mail_type=args['mail_type'], email=args['email'], user_id=args['user_id'])

        if not email:
            abort(409, message="---------------")

        db.session.add(email)
        db.session.commit()
        return email, 201

    @marshal_with(email_address_fields)
    def patch(self, email_id):
        args = email_update_args.parse_args()
        email = EmailAddressModel.query.filter_by(id=email_id).first()
        email_field = args['email']
        if email_field.find('@') == -1:
            abort(404, message='email адрес должен содержать @')
        if not email:
            abort(404, message="Email doesn't exist, cannot update")
        # if args['type_of_mail'] != 'Личная':
        #     abort(404, message="Неправильный тип почты. Личная/Рабочий")
        # if args['type_of_mail'] != 'Рабочий':
        #     abort(404, message="Неправильный тип почты. Личная/Рабочий")
        if args['mail_type']:
            email.mail_type = args['mail_type']
        if args['email']:
            email.email = args['email']

        db.session.commit()

        return email

    def delete(self, email_id):
        email = EmailAddressModel.query.filter(EmailAddressModel.id == email_id).first()
        if not email:
            abort(400, message={'No telephones with this id'})

        db.session.delete(email)
        db.session.commit()
        return '', 204
