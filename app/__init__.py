import os
from flask import Flask
from flask.ext.babel import Babel
from flask.ext.login import LoginManager
from flask.ext.mail import Mail
from flask.ext.openid import OpenID
from flask.ext.sqlalchemy import SQLAlchemy

from config import basedir
from config import ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD
from momentjs import MomentJS

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

oid = OpenID(app, os.path.join(basedir, 'tmp'))

mail = Mail(app)

babel = Babel(app)

app.jinja_env.globals['MomentJS'] = MomentJS

if not app.debug:
    import logging
    from handlers import TlsSMTPHandler
    from logging.handlers import RotatingFileHandler

    app.logger.setLevel(logging.INFO)

    # Email logging
    credentials = None
    if MAIL_USERNAME or MAIL_PASSWORD:
        credentials = (MAIL_USERNAME, MAIL_PASSWORD)
    mail_handler = TlsSMTPHandler(
        (MAIL_SERVER, MAIL_PORT), MAIL_USERNAME, ADMINS, 'microblog failure',
        credentials)
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)

    # File logging
    file_handler = RotatingFileHandler(
        'tmp/microblog.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(
        logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
            )
        )
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('microblog startup')

from app import models, views
