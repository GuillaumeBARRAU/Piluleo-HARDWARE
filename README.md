Définition du projet :

Nous travaillons en équipe sur un système de pilulier, je m’occupe de la partie du RASPBERRY.
Le but est de fournir des médicaments et de savoir si la personne les a bien pris.
le système tournera 1 fois par jour. Le système s’ouvrira automatiquement pour que le patient puisse prendre ses médicaments. Il y a 4 compartiments pour les doses quotidiennes (Matin, Midi, soir, Avant de se coucher).
 
Le système HARDWARE comprend 4 éléments différents :
-	3 boutons, ON/OFF – REMOTE – URGENCE
-	2 LED (rouge et bleu)
-	Un moteur pas à pas
-	4 électro-aimants

Voici les différents fichiers pour qu’il puisse fonctionner : 

1.	Fichier Main
Il va gérer la liaison entre tous les fichiers suivants et la future application.

2.	Fichier Config est le suivant :

Fichier de configuration des pins GPIO et des emails
  Pins pour le moteur pas à pas
   MOTOR_PINS = [18, 23, 24, 25]
  Pin pour le bouton POWER et sa LED
   POWER_BUTTON_PIN = 16
   POWER_LED_PIN = 12
  Pin pour le bouton CONNECT et sa LED
   CONNECT_BUTTON_PIN = 27
   CONNECTION_LED_PIN = 17
  Pin pour le bouton d'urgence (ALERT)
   ALERT_BUTTON_PIN = 4
  Pins pour les électro-aimants
    ELECTROMAGNET_PINS = {
     "MATIN": 26,
     "MIDI": 19,
     "SOIR": 21,
     "AVANT_COUCHER": 20
}
   Configuration des emails
     EMAIL_SENDER = "ton_adresse_gmail@gmail.com"
     EMAIL_PASSWORD = "ton_mot_de_passe"  # Remplace ceci par le mot de passe de ton application
     EMAIL_RECIPIENT = "g.barrau@it-students.fr"

3.	Fichier Bouton_Toggle :
il gère la fonction appuyer : ACTION, tu réappuies : AUTRE ACTION
4.	Fichier Bouton_Hold :
Il gère la fonction maintenir : ACTION tu lâches AUTRE ACTION
5.	Fichier Led_TOGGLE : 
Il gère la fonction de la LED, allumer éteindre

6.	Fichier Led_Pulse :
Il gère la fonction clignotante de la LED

7.	Fichier Power :
Il est lié au fichier Bouton_Toggle et le Fichier Led_Toggle
Il permettra d’allumer ou éteindre le pilulier

8.	Fichier Remote : 
Il est lié au fichier au Fichier Bouton_Toggle,  Fichier Bouton_Hold, Led_Pulse  et le Fichier Led_O_F
Il permet d’allumer ou éteindre le mode REMOTE 
En maintenant il permet de connecter le pilulier à l’application, la LED clignote 

9.	Fichier Alert :
Il est lié au fichier Bouton_Toggle
En appuyant ça envoie un mail d’urgence, mais en appuyant plusieurs fois ça n’envoie pas plusieurs mails (éviter le spam). On va mettre en place un timer entre 2 messages.

10. Fichier Electro_aimant :
Il gère leur fonctionnalité, 2 modes : mode manuel (la personne qui pourra remplir le pilulier), mode automatique (il s'ouvira aux heures données par l'admin)

11.	Fichier RotateStepMotor :
Il permet la rotation du moteur. Le fichier ressemble à ça :

import RPi.GPIO as GPIO
import time
import config

class RotateStepMotor:
    def __init__(self, in1, in2, in3, in4):
        self.IN1 = in1
        self.IN2 = in2
        self.IN3 = in3
        self.IN4 = in4

        # Configurer les broches GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.IN3, GPIO.OUT)
        GPIO.setup(self.IN4, GPIO.OUT)

        # Séquence pour le moteur pas à pas (demi-pas)
        self.step_sequence = [
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 1],
            [1, 0, 0, 1],
        ]

        # Nombre de pas par position
        self.steps_per_position = [73, 73, 73, 73, 73, 73, 73, 74]

    def set_step(self, step):
        GPIO.output(self.IN1, step[0])
        GPIO.output(self.IN2, step[1])
        GPIO.output(self.IN3, step[2])
        GPIO.output(self.IN4, step[3])

    def move_one_step(self):
        # Faire avancer le moteur de manière continue, position par position
        for step in self.step_sequence:
            self.set_step(step)
            time.sleep(0.01)  # Ajustez la vitesse de rotation ici

    def move_automatically(self):
        while True:
            for position in range(len(self.steps_per_position)):
                print(f"Déplacement vers la position {position}")
                steps = self.steps_per_position[position]
                for _ in range(steps):
                    self.move_one_step()

                time.sleep(5)  # Attendre 5 secondes entre chaque mouvement

    def cleanup(self):
        GPIO.cleanup()


Informations supplémentaires :

-	Les compartiments peuvent être ouvert manuellement par le médecin par exemple.
-	Pour les essais le moteur tournera tout seul toutes les 5 secondes.



