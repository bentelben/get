import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 1
signal_frequency = 1
sampling_frequency = 10

try:
    dac = r2r.R2R_DAC(r2r.pins, r2r.max_voltage)
    while True:
        dac.set_voltage(sg.get_sin_wave_amplitude(signal_frequency, time.time()))
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    dac.deinit()