'''
    This is a simple file that shows you the minimal elements you need 
    to write your own experimental sequence.
'''
import numpy as np
from labscript import (
    AnalogIn,
    AnalogOut,
    ClockLine,
    DDS,
    DigitalOut,
    MHz,
    Shutter,
    StaticDDS,
    WaitMonitor,
    start,
    stop,
    wait,
)
from labscriptlib.JosiahApparatus.connection_table import ConnectionTable

if __name__ == '__main__':

    ConnectionTable()

    # Begin issuing labscript primitives.
    # Start() elicits the commencement of the shot.
    dt = 1e-4
    rate = 1 / dt
    start()
    t = 0
    analog1.constant(t=t, value=0)
    t += 200 * dt
    analog1.constant(t=t, value=2)
    t += 200 * dt
    analog1.ramp(t=t, duration=1000 * dt, initial=0, final=5, samplerate=rate)
    t += 1001 * dt
    analog1.ramp(t=t, duration=1000 * dt, initial=5, final=0, samplerate=rate)
    t += 1001 * dt
    analog1.sine(t=t, duration=2000 * dt, amplitude=5, angfreq=50 *
                 np.pi, phase=0, dc_offset=0, samplerate=rate)
    t += 2001 * dt
    analog1.constant(t=t, value=0)
    t += dt
    stop(t=t)
