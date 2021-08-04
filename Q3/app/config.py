import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #mysql://username:password@host:port/db_name
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'site.sqlite')
    SQLALCHEMY_DATABASE_URI = 'mysql://admin:qqqqq11111Q@database-1.cluster-cqpe0uu570ho.us-east-1.rds.amazonaws.com:3306/hk01vote?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_CHARSET='utf8'