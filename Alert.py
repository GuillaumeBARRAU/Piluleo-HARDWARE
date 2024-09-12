# Alert.py

import smtplib
from email.mime.text import MIMEText
from Config import EMAIL_CONFIG

def send_alert_email():
    msg = MIMEText("Alerte ! Un bouton a été pressé.")
    msg['Subject'] = 'Alerte'
    msg['From'] = EMAIL_CONFIG["sender_email"]
    msg['To'] = EMAIL_CONFIG["receiver_email"]

    try:
        with smtplib.SMTP(EMAIL_CONFIG["smtp_server"], EMAIL_CONFIG["smtp_port"]) as server:
            server.starttls()
            server.login(EMAIL_CONFIG["sender_email"], EMAIL_CONFIG["password"])
            server.send_message(msg)
            print("Email d'alerte envoyé.")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email : {e}")
