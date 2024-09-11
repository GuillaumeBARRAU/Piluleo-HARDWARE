import smtplib
from email.mime.text import MIMEText
from Bouton_Toggle import PushButton
import Config

class Alert:
    def __init__(self, button_pin):
        self.button = PushButton(button_pin, self.send_alert)

    def send_alert(self, channel):
        try:
            msg = MIMEText("Alerte : Appel d'urgence requis.")
            msg['Subject'] = "Urgence médicale"
            msg['From'] = Config.EMAIL_SENDER
            msg['To'] = Config.EMAIL_RECIPIENT

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(Config.EMAIL_SENDER, Config.EMAIL_PASSWORD)
                server.sendmail(Config.EMAIL_SENDER, [Config.EMAIL_RECIPIENT], msg.as_string())

        except Exception as e:
            print(f"Erreur lors de l'envoi de l'email: {e}")

    def cleanup(self):
        self.button.cleanup()
