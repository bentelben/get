import mcp4725_driver as mcp
import signal_generator as sg
import time

amplitude = 1
signal_frequency = 1
sampling_frequency = 10

try:
    dac = mcp.MCP4725(5)
    while True:
        dac.set_voltage(sg.get_sin_wave_amplitude(signal_frequency, time.time()))
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    dac.deinit()