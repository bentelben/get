import pwm_dac
import signal_generator as sg
import time

amplitude = 2
signal_frequency = 1
sampling_frequency = 10

try:
    dac = pwm_dac.PWM_DAC(12, 2000, 3.3)
    while True:
        dac.set_voltage(sg.get_sin_wave_amplitude(signal_frequency, time.time()))
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    dac.deinit()