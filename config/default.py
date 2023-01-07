from os.path import abspath, dirname, join


# Definir el directorio de la aplicación
BASE_DIR = dirname(dirname(abspath(__file__)))

# Media dir
MEDIA_DIR = join(BASE_DIR, 'media')
ICONS_IMAGES_DIR = join(MEDIA_DIR, 'icons')
LOGOS_IMAGES_DIR = join(MEDIA_DIR, 'logos')
ITEMS_IMAGES_DIR = join(MEDIA_DIR, 'items')

SECRET_KEY = '6dca48775e39cabec10b45c19b1f43bcc0708ce9ab64e5c12b885174c0a957bff2fb624174ea15aa'

# Configuración de base de datos
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Entornos de aplicaciones
APP_ENV_LOCAL = 'local'
APP_ENV_TESTING = 'testing'
APP_ENV_DEVELOPMENT = 'development'
APP_ENV_STAGING = 'staging'
APP_ENV_PRODUCTION = 'production'
APP_ENV = ''

# Configuración del email
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USERNAME = 'lahozcristian@gmail.com'
MAIL_PASSWORD = 'xkintnosllquungb' # password de aplicación generado por google
DONT_REPLY_FROM_EMAIL = '(Cristian, lahozcristian@gmail.com)'
ADMINS = ('lahozcristian@gmail.com', )
MAIL_USE_TLS = True
MAIL_DEBUG = False

# Configurar Paginación
ITEMS_PER_PAGE = 3