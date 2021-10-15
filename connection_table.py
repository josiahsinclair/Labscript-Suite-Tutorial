# Import some useful functions and packages
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

# Import the relevant devices from labscript_devices
from labscript_devices.PrawnBlaster.labscript_devices import PrawnBlaster
from labscript_devices.NI_DAQmx.labscript_devices import NI_PCI_6713


def ConnectionTable():

    PrawnBlaster(
        name="prawnblaster_0",
        com_port="COM6",
        num_pseudoclocks=2,
    )

    NI_PCI_6713(
        name="ni_card_1",
        parent_device=prawnblaster_0.clocklines[0],
        clock_terminal="/Dev1/PFI0",
        MAX_name="Dev1",
    )

    # Create the output/input channels on the above devices use the example1 conversion
    # class located in pythonlib/unitconversions/example.py with default paremeters
    AnalogOut(
        name="analog0",
        parent_device=ni_card_1,
        connection="ao0",
    )
    AnalogOut(
        name="analog1",
        parent_device=ni_card_1,
        connection="ao1",
    )


if __name__ == '__main__':
    ConnectionTable()
    # Begin issuing labscript primitives
    # start() elicits the commencement of the shot
    start()
    # Stop the experiment shot with stop()
    stop(1.0)
