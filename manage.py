# https://code.visualstudio.com/docs/python/debugging
# import ptvsd

# Allow other computers to attach to ptvsd at this IP address and port.
#ptvsd.enable_attach(address=('172.28.0.1', 3000), redirect_output=True)

# Pause the program until a remote debugger is attached
#ptvsd.wait_for_attach()

from app.main import model
import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.main import create_app, db

app = create_app(os.getenv('ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.option('-h', '--host', dest='host', default='127.0.0.1')
@manager.option('-p', '--port', dest='port', default=5000)
def run(host, port):
    app.run(host=host, port=port)


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
