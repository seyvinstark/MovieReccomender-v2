import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
TOP_LEVEL_DIR = os.path.abspath(os.curdir)




SECRET_KEY = "thisisthesecretkeyhere"
SQLALCHEMY_DATABASE_URI  = "mysql://root:annemuhiza@localhost/movies"




RECAPTCHA_PUBLIC_KEY = '6LdYIDcUAAAAAEE3N3tNqcYu50MJSTlGA5lwu5Pl'
RECAPTCHA_PRIVATE_KEY = '6LdYIDcUAAAAAD8ayN_2Mkhauh_-MdK12XxdTLEo'


# Uploads
UPLOADS_DEFAULT_DEST = TOP_LEVEL_DIR + '/project/static/img/'
UPLOADS_DEFAULT_URL = 'http://localhost:5000/static/img/'
 
UPLOADED_IMAGES_DEST = TOP_LEVEL_DIR + '/project/static/img/'
UPLOADED_IMAGES_URL = 'http://localhost:5000/static/img/'

