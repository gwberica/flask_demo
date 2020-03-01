from flask import session

from flask_script import Manager
from info import create_app, db
from flask_migrate import Migrate, MigrateCommand

app = create_app(environ="dev")

manage = Manager(app)
Migrate(app, db)
manage.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manage.run()
