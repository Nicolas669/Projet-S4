# p = GPIO.PWM(broche, frequence= f)
# p.start(rapport_cyclique)
# rapport_cyclique RC entre 0 et 100 = le signal sera à HIGH pendant RC % du cycle de 1/f secondes

import RPi.GPIO as GPIO
import time


class Robot:
    """ classe permettant de controler le robot """

    def __init__(self, gpio1_roue_droite, gpio2_roue_droite, gpio_pwm_roue_droite, gpio1_roue_gauche, gpio2_roue_gauche, gpio_pwm_roue_gauche):
        # roue droite du robot
        self.gpio1_roue_droite = gpio1_roue_droite
        self.gpio2_roue_droite = gpio2_roue_droite
        self.gpio_pwm_roue_droite = gpio_pwm_roue_droite
        
        # roue gauche du robot
        self.gpio1_roue_gauche = gpio1_roue_gauche
        self.gpio2_roue_gauche = gpio2_roue_gauche
        self.gpio_pwm_roue_gauche = gpio_pwm_roue_gauche

        # initialisation
        GPIO.setup(self.gpio1_roue_gauche, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.gpio2_roue_gauche, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.gpio1_roue_droite, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.gpio2_roue_droite, GPIO.OUT, initial=GPIO.LOW)

        GPIO.setup(gpio_pwm_roue_droite, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(gpio_pwm_roue_gauche, GPIO.OUT, initial=GPIO.LOW)
        self.pwm_roue_droite = GPIO.PWM(gpio_pwm_roue_droite, 8)  # frequence = 8
        self.pwm_roue_gauche = GPIO.PWM(gpio_pwm_roue_gauche, 8)
        self.pwm_roue_droite.start(0)  # rapport cyclique = 0
        self.pwm_roue_gauche.start(0)

    def avancer_droit(self, temps):
        """ le robot avance tout droit pendant temps secondes
        temps = entier = temps en secondes """
        GPIO.output(self.gpio1_roue_droite, GPIO.HIGH)
        GPIO.output(self.gpio2_roue_droite, GPIO.LOW)
        
        GPIO.output(self.gpio1_roue_gauche, GPIO.HIGH)
        GPIO.output(self.gpio2_roue_gauche, GPIO.LOW)
        
        time.sleep(temps)

        GPIO.output(self.gpio1_roue_droite, GPIO.LOW)
        GPIO.output(self.gpio2_roue_droite, GPIO.LOW)

        GPIO.output(self.gpio1_roue_gauche, GPIO.LOW)
        GPIO.output(self.gpio2_roue_gauche, GPIO.LOW)

    def reculer_droit(self, temps):
        """ le robot recule tout droit pendant temps secondes
        temps = entier = temps en secondes """
        GPIO.output(self.gpio1_roue_droite, GPIO.LOW)
        GPIO.output(self.gpio2_roue_droite, GPIO.HIGH)

        GPIO.output(self.gpio1_roue_gauche, GPIO.LOW)
        GPIO.output(self.gpio2_roue_gauche, GPIO.HIGH)

        time.sleep(temps)

        GPIO.output(self.gpio1_roue_droite, GPIO.LOW)
        GPIO.output(self.gpio2_roue_droite, GPIO.LOW)

        GPIO.output(self.gpio1_roue_gauche, GPIO.LOW)
        GPIO.output(self.gpio2_roue_gauche, GPIO.LOW)
