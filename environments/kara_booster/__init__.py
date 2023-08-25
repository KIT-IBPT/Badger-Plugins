import time
from typing import List

import numpy as np
from badger import environment
from badger.interface import Interface

# array containing names of the beam currents. Used to communicate with SoftIOC and epics.
OBSERVABLES = [
    "A:BO:DTACQChannel:BeamCurrent:Max",
    "A:BO:DTACQChannel:BeamCurrent:Extraction:Mean",
    "A:SR:BeamInfo:01:Current",
    "CURRENT_RATIO"
]


# environment containing all the process variables and objective functions for the KARA Microtron
class Environment(environment.Environment):
    name = "Kara_Injection_Line"

    vranges = {
        "A:BO:PS:MCH-01:Current:Setpoint": [-2.0, 2.0],
        "A:BO:PS:MCH-02:Current:Setpoint": [-2.0, 2.0],
        "A:BO:PS:MCH-03:Current:Setpoint": [-2.0, 2.0],
        "A:BO:PS:MCH-04:Current:Setpoint": [-2.0, 2.0],
        "A:BO:PS:MCV-01:Current:Setpoint": [-2.0, 2.0],
        "A:BO:PS:MCV-02:Current:Setpoint": [-2.0, 2.0],
        "A:BO:PS:MCV-03:Current:Setpoint": [-2.0, 2.0],
        "A:BO:PS:MCV-04:Current:Setpoint": [-2.0, 2.0],
        "A:BO:PS:MQ-01:Current:Setpoint": [0.0, 120.0],
        "A:BO:PS:MB-01:Current:Setpoint": [0.0, 866.0],
        "A:BO:PS:MKick-01:Hvps:Voltage:Setpoint": [0, 350.0],
        "A:BO:PS:MKick-02:Hvps:Voltage:Setpoint": [0, 1000.0],
        "A:BO:PS:MSept-01:Hvps:Voltage:Setpoint": [0, 200.0],
        "A:BO:PS:MSept-02:Hvps:Voltage:Setpoint": [0, 1000.0],
        "A:BO:PS:MBump-01:Current:Setpoint": [-12.0, 12.0],
        "A:BO:PS:MBump-02:Current:Setpoint": [-12.0, 12.0],
    }

    def __init__(self, interface: Interface, params):
        super().__init__(interface, params)

    @staticmethod
    def list_vars():
        # Returns the names of the actuators
        return [
            "A:BO:PS:MCH-01:Current:Setpoint",
            "A:BO:PS:MCH-02:Current:Setpoint",
            "A:BO:PS:MCH-03:Current:Setpoint",
            "A:BO:PS:MCH-04:Current:Setpoint",
            "A:BO:PS:MCV-01:Current:Setpoint",
            "A:BO:PS:MCV-02:Current:Setpoint",
            "A:BO:PS:MCV-03:Current:Setpoint",
            "A:BO:PS:MCV-04:Current:Setpoint",
            "A:BO:PS:MQ-01:Current:Setpoint",
            "A:BO:PS:MB-01:Current:Setpoint",
            "A:BO:PS:MKick-01:Hvps:Voltage:Setpoint",
            "A:BO:PS:MKick-02:Hvps:Voltage:Setpoint",
            "A:BO:PS:MSept-01:Hvps:Voltage:Setpoint",
            "A:BO:PS:MSept-02:Hvps:Voltage:Setpoint",
            "A:BO:PS:MBump-01:Current:Setpoint",
            "A:BO:PS:MBump-02:Current:Setpoint",
        ]

    @staticmethod
    def list_obses():
        # array of the names of all observables #
        return OBSERVABLES

    def _get_vrange(self, var):
        # [min, max] of the actuator
        return self.vranges[var]

    def _get_var(self, var):
        return self.interface.get_value(var)

    def _set_var(self, var, x):
        if not self.params["read_only"]:
            self.interface.set_value(var, x)

    def _get_obs(self, obs):
        observations = []
        for _ in range(int(self.params["n_average"])):
            if (obs == "CURRENT_RATIO"):
                observations.append(self.interface.get_value("A:BO:DTACQChannel:BeamCurrent:Extraction:Mean") / self.interface.get_value("A:BO:DTACQChannel:BeamCurrent:Max") )
            else:
                observations.append(self.interface.get_value(obs))
            time.sleep(1.0)
        avg_obs = np.mean(observations)
        return avg_obs

    @staticmethod
    def get_default_params():
        return {
            "waiting_time": 1.0,  # delay between setting a variable and reading the observables
            "read_only": False,
            "n_average": 1,
        }

    def vars_changed(self, vars: List[str], values: list):
        time.sleep(self.params["waiting_time"])
