import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DATA_PATH = os.path.join('data', 'data.csv')
