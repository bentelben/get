import RPi.GPIO as GPIO

pins = [22, 27, 17, 26, 25, 21, 20, 16]
max_voltage = 3.191

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()
    
    def number_to_dac(self, number):
        if self.verbose:
            print(f"setting {number/(2**len(self.gpio_bits)-1)*self.dynamic_range}")
        binValue = bin(number)[2:].zfill(len(self.gpio_bits))[::-1]
        for i in range(len(self.gpio_bits)):
            GPIO.output(self.gpio_bits[i], binValue[i] == '1')

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            if self.verbose:
                print(f"voltage {voltage} not in range [0; {self.dynamic_range}]")
            return 0
        number = int (voltage / self.dynamic_range * (2**len(self.gpio_bits)-1))
        self.number_to_dac(number)

if __name__ == '__main__':
    try:
        dac = R2R_DAC(pins, max_voltage, True)
        while True:
            try:
                voltage = float(input())
                dac.set_voltage(voltage)
            except ValueError:
                print("not number")
    finally:
        dac.deinit()