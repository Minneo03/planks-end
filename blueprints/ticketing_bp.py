from flask import Blueprint, render_template, request, redirect, url_for, flash
from databaseConnection import get_db_connection

ticketing_bp = Blueprint('ticketing_bp', __name__)


@ticketing_bp.route('/ticketing', methods=['GET', 'POST'])
def ticketing():
    if request.method == 'POST':
        purchaser_email = request.form['purchaser_email']
        customer_names = request.form.getlist('customer_name[]')
        age_categories = request.form.getlist('age_category[]')

        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert each customer as a new record
        for name, age in zip(customer_names, age_categories):
            cursor.execute(
                'INSERT INTO tickets (customer_name, age_category, purchaser_email) VALUES (?, ?, ?)',
                (name, age, purchaser_email)
            )

        conn.commit()
        conn.close()

        flash("Tickets booked successfully!")
        return redirect(url_for('ticketing_bp.ticketing'))

    return render_template('pages/ticketing.html')
