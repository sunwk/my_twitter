from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from models import db

from models.user import User
from models.tweet import Tweet
from models.comment import Comment

from routes.showpage import main as routes_showpage
from routes.timeline import main as routes_timeline
from routes.authority import main as routes_auth
from routes.tweet_detail import main as routes_detail
from routes.edit import main as routes_edit

from api.auth import main as api_auth


app = Flask(__name__)
db_path = 'db.sqlite'
manager = Manager(app)


def register_routes(app):
    app.register_blueprint(routes_timeline, url_prefix='/timeline')
    app.register_blueprint(routes_auth, url_prefix='/auth')
    app.register_blueprint(routes_edit, url_prefix='/edit')
    app.register_blueprint(routes_detail, url_prefix='/tweet')
    app.register_blueprint(routes_showpage)
    app.register_blueprint(api_auth, url_prefix='/api')


def configure_app():
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.secret_key = 'secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_path)
    db.init_app(app)
    register_routes(app)


def configured_app():
    configure_app()
    return app


@manager.command
def server():
    print('server run')
    # app = configured_app()
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=3000,
    )
    app.run(**config)


def configure_manager():
    Migrate(app, db)
    manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    configure_manager()
    configure_app()
    # manager.run()
    app.run(debug=True)
# gunicorn -b '0.0.0.0:80' redischat:app
