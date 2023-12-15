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
    "A:AX:DAQDT:05:1:AI:WF:08:V.VALE",
    "A:MI:DTACQChannel:BeamCurrent-EGun:Mean",
    "A:MI:DTACQChannel:BeamCurrent-02:Mean",
    "A:MI:DTACQChannel:BeamCurrent-03:Mean",
    "A:MI:DTACQChannel:BeamCurrent-04:Mean",
    "A:MI:DTACQChannel:BeamCurrent-05:Mean",
    "A:MI:DTACQChannel:BeamCurrent-06:Mean",
    "A:MI:DTACQChannel:BeamCurrent-07:Mean",
    "A:MI:DTACQChannel:BeamCurrent-08:Mean",
]


# environment containing all the process variables and objective functions for the KARA Microtron
class Environment(environment.Environment):
    name = "Kara_Injectors"

    vranges = {
        "A:MI:PS:MCH-08:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCH-09:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCH-10:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCV-08:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCV-09:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCV-10:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MB-11:Current:Setpoint": [0.0, 190.0],
        "A:IL:PS:MCH-01:Current:Setpoint": [-2.0, 2.0],
        "A:IL:PS:MCH-02:Current:Setpoint": [-2.0, 2.0],
        "A:IL:PS:MCH-03:Current:Setpoint": [-2.0, 2.0],
        "A:IL:PS:MCH-04:Current:Setpoint": [-2.0, 2.0],
        "A:IL:PS:MCV-01:Current:Setpoint": [-2.0, 2.0],
        "A:IL:PS:MCV-02:Current:Setpoint": [-2.0, 2.0],
        "A:IL:PS:MCV-03:Current:Setpoint": [-2.0, 2.0],
        "A:IL:PS:MCV-04:Current:Setpoint": [-2.0, 2.0],
        "A:IL:PS:MQ-01:Current:Setpoint": [0.0, 8.0],
        "A:IL:PS:MQ-02:Current:Setpoint": [0.0, 8.0],
        "A:IL:PS:MQ-03:Current:Setpoint": [0.0, 8.0],
        "A:IL:PS:MQ-04:Current:Setpoint": [0.0, 8.0],
        "A:IL:PS:MQ-05:Current:Setpoint": [0.0, 8.0],
        "A:IL:PS:MB-01:Current:Setpoint": [0.0, 95.0],
        "A:BO:PS:MSept-01:Hvps:Voltage:Setpoint": [0, 200],
        "A:TI:SignGen:MI-01:Power": [-10.0, -5.0],
        "A:MI:PS:MCH-01:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCH-03:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCH-04:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCH-05:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCH-06:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCH-07:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCV-01:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCV-02:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCV-03:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCV-04:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCV-05:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCV-06:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCV-07:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MQV-01:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MQV-02:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MSol-01:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MSol-02:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MSol-03:Current:Setpoint": [-2.0, 2.0],
        # 'A:IL:PS:MB-02:Current:Setpoint': [0.0, 95.0], not in KARA registry
    }

    def __init__(self, interface: Interface, params):
        super().__init__(interface, params)

    @staticmethod
    def list_vars():
        # Returns the names of the actuators
        return [
            "A:MI:PS:MCH-08:Current:Setpoint",
            "A:MI:PS:MCH-09:Current:Setpoint",
            "A:MI:PS:MCH-10:Current:Setpoint",
            "A:MI:PS:MCV-08:Current:Setpoint",
            "A:MI:PS:MCV-09:Current:Setpoint",
            "A:MI:PS:MCV-10:Current:Setpoint",
            "A:MI:PS:MB-11:Current:Setpoint",
            "A:IL:PS:MCH-01:Current:Setpoint",
            "A:IL:PS:MCH-02:Current:Setpoint",
            "A:IL:PS:MCH-03:Current:Setpoint",
            "A:IL:PS:MCH-04:Current:Setpoint",
            "A:IL:PS:MCV-01:Current:Setpoint",
            "A:IL:PS:MCV-02:Current:Setpoint",
            "A:IL:PS:MCV-03:Current:Setpoint",
            "A:IL:PS:MCV-04:Current:Setpoint",
            "A:IL:PS:MQ-01:Current:Setpoint",
            "A:IL:PS:MQ-02:Current:Setpoint",
            "A:IL:PS:MQ-03:Current:Setpoint",
            "A:IL:PS:MQ-04:Current:Setpoint",
            "A:IL:PS:MQ-05:Current:Setpoint",
            "A:IL:PS:MB-01:Current:Setpoint",
            "A:BO:PS:MSept-01:Hvps:Voltage:Setpoint",
            "A:TI:SignGen:MI-01:Power",
            "A:MI:PS:MCH-01:Current:Setpoint",
            "A:MI:PS:MCH-03:Current:Setpoint",
            "A:MI:PS:MCH-04:Current:Setpoint",
            "A:MI:PS:MCH-05:Current:Setpoint",
            "A:MI:PS:MCH-06:Current:Setpoint",
            "A:MI:PS:MCH-07:Current:Setpoint",
            "A:MI:PS:MCV-01:Current:Setpoint",
            "A:MI:PS:MCV-02:Current:Setpoint",
            "A:MI:PS:MCV-03:Current:Setpoint",
            "A:MI:PS:MCV-04:Current:Setpoint",
            "A:MI:PS:MCV-05:Current:Setpoint",
            "A:MI:PS:MCV-06:Current:Setpoint",
            "A:MI:PS:MCV-07:Current:Setpoint",
            "A:MI:PS:MQV-01:Current:Setpoint",
            "A:MI:PS:MQV-02:Current:Setpoint",
            "A:MI:PS:MSol-01:Current:Setpoint",
            "A:MI:PS:MSol-02:Current:Setpoint",
            "A:MI:PS:MSol-03:Current:Setpoint",
            # 'A:IL:PS:MB-02:Current:Setpoint': [0.0, 95.0], not in KARA registry
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
