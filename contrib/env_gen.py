"""
Django SECRET_KEY generator.
"""
from django.utils.crypto import get_random_string


chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

CONFIG_STRING = """
DEBUG=True
SECRET_KEY=%s
ALLOWED_HOSTS=127.0.0.1, .localhost,0.0.0.0,.herokuapp.com

#DB_HOST=db
#POSTGRES_DB=mydb
#POSTGRES_USER=myuser
#POSTGRES_PASSWORD=mypass

# or smtp.EmailBackend
#EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
#EMAIL_HOST=
#EMAIL_PORT=587
#EMAIL_HOST_USER=
#EMAIL_HOST_PASSWORD=
#EMAIL_USE_TLS=True
""".strip() % get_random_string(50, chars)

# Writing our configuration file to '.env'
with open('.env', 'w') as configfile:
    configfile.write(CONFIG_STRING)
