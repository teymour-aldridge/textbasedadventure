import os
import secrets

from flask import Flask

from . import db, auth, story


def create_app(test_config=None):
    # Create and configure app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=secrets.token_hex(512),
        DATABASE=os.path.join(app.instance_path, 'textbasedadventure.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return '<h1>Hello World!<h1>'

    db.init_app(app)

    app.register_blueprint(auth.bp)

    app.register_blueprint(story.bp)
    app.add_url_rule('/', endpoint='index')

    return app
