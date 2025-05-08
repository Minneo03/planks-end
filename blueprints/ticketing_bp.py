from flask import Blueprint, render_template, request, redirect, url_for, flash
from databaseConnection import get_db_connection
from email_utils import send_email

ticketing_bp = Blueprint('ticketing_bp', __name__)

@ticketing_bp.route('/ticketing', methods=['GET', 'POST'])
def ticketing():
    if request.method == 'POST':
        purchaser_email = request.form['purchaser_email']
        customer_names = request.form.getlist('customer_name[]')
        age_categories = request.form.getlist('age_category[]')

        # Calculate the total price: Adults $39.99, Children $19.99
        adult = 0.0
        child = 0.0
        for age in age_categories:
            if (age == "Adult"):
                adult += 1
            if (age == "Child"):
                child += 1

        total_price = (adult * 39.99) + (child * 19.99)

        # Establish the database connection
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            'INSERT INTO Orders (email, totalPrice) VALUES (?, ?)',
            (purchaser_email, total_price)
        )
        order_id = cursor.lastrowid

        # Insert each ticket from the order into the Tickets table
        for name in customer_names:
            cursor.execute(
                'INSERT INTO Tickets (orderID, name) VALUES (?, ?)',
                (order_id, name)
            )

        message = "The tickets are for " + str(customer_names) + " who owe $" + str(round(total_price, 2)) + " dollars."
        send_email('Tickets for Plank\'s End!', purchaser_email, message)
        conn.commit()
        conn.close()

        flash("Tickets booked successfully!")
        return redirect(url_for('ticketing_bp.ticketing'))

    return render_template('pages/ticketing.html')


