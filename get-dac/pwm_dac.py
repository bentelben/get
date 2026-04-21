import RPi.GPIO as GPIO

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 0)
    
        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        self.pwm.start(0)
    
    def set_voltage(self, voltage):
        if not (0 <= voltage <= self.dynamic_range):
            print('not in range')
            voltage = 0
        self.pwm.ChangeDutyCycle(voltage/self.dynamic_range*100)
    
    def deinit(self):
        self.pwm.stop()
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()

if __name__ == '__main__':
    try:
        dac = PWM_DAC(12, 1000, 3.3, True)
        
        while True:
            try:
                voltage = float(input())
                dac.set_voltage(voltage)
            except ValueError:
                print('not number')
            
    finally:
        dac.deinit()