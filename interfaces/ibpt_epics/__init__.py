import time

import numpy as np
from badger import interface
from ibpt.epics import PV


class Interface(interface.Interface):
    name = "ibpt_epics"

    def __init__(self, params=None):
        super().__init__(params)

        self.pvs = {}  # Dictionary of PVs

    @staticmethod
    def get_default_params():
        return None

    @interface.log
    def get_value(self, channel: str, as_string=False):
        try:
            pv = self.pvs[channel]
        except KeyError:  # Add a new PV
            pv = PV(channel)
            self.pvs[channel] = pv

        value = pv.get(as_string=as_string)

        return value

    @interface.log
    def set_value(self, channel: str, value):
        try:
            pv = self.pvs[channel]
        except KeyError:  # Add a new PV
            pv = PV(channel)
            self.pvs[channel] = pv

        # Wait for no longer 5s
        pv.put(value, wait=True, timeout=3)

        _value = pv.get()
        return _value
