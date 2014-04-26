import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLED = True
SECRET_KEY = 'secret-key-goes-here'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

# Mail server settings
MAIL_SERVER = 'smtp.gmail.com'
# MAIL_PORT = 587  # Old port for logging using TlsSMTPHandler
MAIL_PORT = 465  # SSL
MAIL_USERNAME = 'example@gmail.com'
MAIL_PASSWORD = 'password'
MAIL_USE_TLS = False
MAIL_USE_SSL = True

# Administrator list
ADMINS = ['example@gmail.com']

# Pagination
POSTS_PER_PAGE = 3

# Whoosh (search)
WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50
