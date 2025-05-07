from flask import Blueprint, render_template, request, flash, redirect, url_for
from email_utils import send_email

email_bp = Blueprint('email', __name__, template_folder='../templates/pages')

@email_bp.route('/emailTesting', methods=['GET', 'POST'])
def email_testing():
    if request.method == 'POST':
        recipient = request.form['email']
        message = request.form['message']
        try:
            send_email('Test Email from Plank\'s End', recipient, message)
            flash('Email sent successfully!', 'success')
        except Exception as e:
            flash(f'Failed to send email: {str(e)}', 'error')
        return redirect(url_for('email.email_testing'))
    return render_template('emailTesting.html')
