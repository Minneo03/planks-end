from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('pages/homePage.html')

@app.route('/amusements')
def amusements():
    return render_template('pages/amusements.html')

@app.route('/ticketing')
def ticketing():
    return render_template('pages/ticketing.html')

@app.route('/aboutUs')
def aboutUs():
    return render_template('pages/aboutUs.html')

if __name__ == '__main__':
    app.run(debug=True)
