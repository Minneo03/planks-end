from flask import Flask, render_template
from config import Config
from extensions import mail
from blueprints.email_bp import email_bp
from blueprints.ticketing_bp import ticketing_bp
import os

app = Flask(__name__)
app.config.from_object(Config)

app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

# Initialize Flask-Mail
mail.init_app(app)

# Register blueprints
app.register_blueprint(email_bp, url_prefix='/')
app.register_blueprint(ticketing_bp, url_prefix='/')

@app.route('/')
def home():
    return render_template('pages/homePage.html')

@app.route('/amusements')
def amusements():
    return render_template('pages/amusements.html')

@app.route('/aboutUs')
def aboutUs():
    return render_template('pages/aboutUs.html')

@app.route('/planksEnd')
def planksEnd():
    return render_template('pages/planksEnd.html')

@app.route('/emailTesting')
def emailTesting():
    return render_template('pages/emailTesting.html')

if __name__ == '__main__':
    app.run(debug=True)
