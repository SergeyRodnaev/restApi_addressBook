from flask_restful import Resource, reqparse, abort, fields, marshal_with
from app.models import db, TelephoneModel

telephones_put_args = reqparse.RequestParser()
telephones_put_args.add_argument("phone_type", type=str, choices=('Городской', 'Мобильный'),
                                 help="Телефон может быть только Городской или Мобильный", required=True)
telephones_put_args.add_argument("phone_number", type=str, help="Номер телефона", required=True)
telephones_put_args.add_argument("user_id", type=int, help="id пользователя телефона", required=True)

telephones_update_args = reqparse.RequestParser()
telephones_update_args.add_argument("phone_type", type=str, choices=('Городской', 'Мобильный'),
                                    help="Телефон может быть только Городской или Мобильный")
telephones_update_args.add_argument("phone_number", type=str, help="Номер телефона")

telephones_fields = {
    'id': fields.Integer,
    'phone_type': fields.String,
    'phone_number': fields.String,
    'user_id': fields.Integer
}


class Telephones(Resource):
    @marshal_with(telephones_fields)
    def post(self, sort_field=None):
        telephone = TelephoneModel.query.order_by(sort_field).all()

        return telephone

    @marshal_with(telephones_fields)
    def put(self):
        args = telephones_put_args.parse_args()

        telephone = TelephoneModel(phone_type=args['phone_type'], phone_number=args['phone_number'],
                                   user_id=args['user_id'])

        db.session.add(telephone)
        db.session.commit()
        return telephone, 201

    @marshal_with(telephones_fields)
    def patch(self, telephones_id):
        args = telephones_update_args.parse_args()

        telephone = TelephoneModel.query.filter_by(id=telephones_id).first()

        if not telephone:
            abort(404, message="Telephones doesn't exist, cannot update")

        if args['phone_type']:
            telephone.phone_type = args['phone_type']
        if args['phone_number']:
            telephone.phone_number = args['phone_number']

        db.session.commit()

        return telephone

    def delete(self, telephones_id):
        telephone = TelephoneModel.query.filter(TelephoneModel.id == telephones_id).first()
        if not telephone:
            abort(400, message={'No telephones with this id'})

        db.session.delete(telephone)
        db.session.commit()
        return '', 204
