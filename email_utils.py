from flask_mail import Message
from extensions import mail

def send_email(subject, recipient, body):
    msg = Message(subject, sender="noreply@planksend.com", recipients=[recipient])
    msg.body = body
    mail.send(msg)
