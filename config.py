import os

class Config:
    SECRET_KEY = 'pla4n!ksEn%d_1ver^y_se7c&ret_key5.*Yes&3sir'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')  # Im using environment variables for security,
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')  # but this also means it only works in my dev environment at the moment.
