import os

class Config(object):
    SECRET_KY = os.environ.get('SECRET_KEY') or "helina_fidah_Secret"