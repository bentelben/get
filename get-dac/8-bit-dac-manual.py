import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pins = [22, 27, 17, 26, 25, 21, 20, 16]

GPIO.setup(pins, GPIO.OUT)

dynamicRange = 3.191

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamicRange):
        print(f"voltage {voltage} not in range [0; {dynamicRange}]")
        return 0
    return int (voltage / dynamicRange * (2**len(pins)-1))

def number_to_dac(number):
    print(f"setting {number/(2**len(pins)-1)*dynamicRange}")
    binValue = bin(number)[2:].zfill(len(pins))[::-1]
    for i in range(len(pins)):
        GPIO.output(pins[i], binValue[i] == '1')

GPIO.output(pins, 0)
try:
    while True:
        try:
            voltage = float(input())
            number_to_dac(voltage_to_number(voltage))
        except ValueError:
            pass
finally:
    GPIO.output(pins, 0)
    GPIO.cleanup()