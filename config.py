import os

SECRET_KEY = 'cadastro'

# database configurations
MYSQL_HOST = '127.0.0.1'
MYSQL_USER = 'flask_user'
MYSQL_PASSWORD = 'flask_Password123'
MYSQL_DB = 'cadastro'
MYSQL_PORT = 3306
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads' # path to upload directory