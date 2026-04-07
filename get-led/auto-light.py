import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

led = 27
photoresistor = 6

GPIO.setup(led, GPIO.OUT)
GPIO.setup(photoresistor, GPIO.IN)

while True:
    GPIO.output(led, not GPIO.input(photoresistor))