# Fichier de configuration des pins GPIO et des emails

# Pins pour le moteur pas à pas
MOTOR_PINS = [18, 23, 24, 25]

# Pin pour le bouton POWER et sa LED
POWER_BUTTON_PIN = 16
POWER_LED_PIN = 12

# Pin pour le bouton CONNECT et sa LED
CONNECT_BUTTON_PIN = 27
CONNECTION_LED_PIN = 17

# Pin pour le bouton d'urgence (ALERT)
ALERT_BUTTON_PIN = 4

# Pins pour les électro-aimants
ELECTROMAGNET_PINS = {
    "MATIN": 26,
    "MIDI": 19,
    "SOIR": 21,
    "AVANT_COUCHER": 20
}

# Configuration des emails
EMAIL_SENDER = "ton_adresse_gmail@gmail.com"
EMAIL_PASSWORD = "ton_mot_de_passe"
EMAIL_RECIPIENT = "g.barrau@it-students.fr"
