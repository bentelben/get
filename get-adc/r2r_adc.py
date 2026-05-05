import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)
    
    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def number_to_dac(self, number):
        binValue = bin(number)[2:].zfill(len(self.bits_gpio))
        for i in range(len(self.bits_gpio)):
            GPIO.output(self.bits_gpio[i], binValue[i] == '1')
    
    def sequential_counting_adc(self):
        for i in range(0, 2**len(self.bits_gpio)):
            self.number_to_dac(i)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio):
                return i
        
        return 2**len(self.bits_gpio)-1
    
    def get_sc_voltage(self):
        return self.sequential_counting_adc()/(2**len(self.bits_gpio)-1)*self.dynamic_range
    
    def successive_approximation_adc(self):
        num = 0
        for i in range(0, len(self.bits_gpio)):
            offset = 2**(len(self.bits_gpio) - 1 - i)
            self.number_to_dac(num + offset)
            time.sleep(self.compare_time)
            if not GPIO.input(self.comp_gpio):
                num += offset
        return num
    
    def get_sar_voltage(self):
        return self.successive_approximation_adc()/(2**len(self.bits_gpio)-1)*self.dynamic_range

if __name__ == '__main__':
    try:
        adc = R2R_ADC(3.2)
        adc.number_to_dac(2**len(adc.bits_gpio)-1)
        input()

        while True:
            #print(adc.get_sc_voltage())
            print(adc.get_sar_voltage())
            time.sleep(0.5)
    finally:
        adc.deinit()