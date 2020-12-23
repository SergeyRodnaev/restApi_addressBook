from app.app import api, app, db
from app.views.email_views import EmailAddress
from app.views.telephones_views import Telephones
from app.views.user_views import User
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

api.add_resource(User, '/user',
                 '/user/sort_field=<sort_field>',
                 '/user/id=<int:user_id>')
api.add_resource(Telephones, '/telephones',
                 '/telephones/sort_field=<sort_field>',
                 '/telephones/id=<int:telephones_id>')
api.add_resource(EmailAddress, '/email',
                 '/email/sort_field=<sort_field>',
                 '/email/id=<int:email_id>')

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
