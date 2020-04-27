from flask import Flask,g,session
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager


from models import db, timestamp



app = Flask(__name__)
manager = Manager(app)


def configured_app():
    import config
    app.secret_key = config.secret_key
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:xhb13512551467@localhost/bbs'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bbs.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)
    register_routes(app)
    return app


def configure_manager():
    Migrate(app,db)
    manager.add_command('db',MigrateCommand)


def register_routes(app):
    # from routes.node import main as routes_node
    # from routes.topic import main as routes_topic
    from routes.index import main as routes_index
    # from routes.user import main as routes_user
    # from routes.comment import main as routes_comment
    #
    #
    app.register_blueprint(routes_index)
    # app.register_blueprint(routes_node,url_prefix='/node')
    # app.register_blueprint(routes_topic)
    # app.register_blueprint(routes_user, url_prefix='/user')
    # app.register_blueprint(routes_comment, url_prefix='/comment')
    pass


@manager.command
def server():
    print('server run')
    config = dict(
        debug=True,
        host='',
        port=3000,
    )
    app.run(**config)


if __name__ == '__main__':
    configure_manager()
    configured_app()
    manager.run()

