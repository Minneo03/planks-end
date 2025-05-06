from flask import Flask
from flask_cors import CORS
from routes.amusements import amusements_bp
from routes.tickets import tickets_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(amusements_bp, url_prefix='/api/amusements')
app.register_blueprint(tickets_bp, url_prefix='/api/tickets')

if __name__ == '__main__':
    app.run(debug=True)
