import time
from typing import List

from badger import environment
from badger.interface import Interface

OBSERVALBES = [
    "A:MI:DTACQChannel:BeamCurrent-EGun:Mean",
    "A:MI:DTACQChannel:BeamCurrent-02:Mean",
    "A:MI:DTACQChannel:BeamCurrent-03:Mean",
    "A:MI:DTACQChannel:BeamCurrent-04:Mean",
    "A:MI:DTACQChannel:BeamCurrent-05:Mean",
    "A:MI:DTACQChannel:BeamCurrent-06:Mean",
    "A:MI:DTACQChannel:BeamCurrent-07:Mean",
    "A:MI:DTACQChannel:BeamCurrent-08:Mean",
]


# environment for KARA Microtron tuning
class Environment(environment.Environment):
    name = "Kara_Microtron"

    vranges = {
        "A:MI:PS:MCH-01:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCH-03:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCH-04:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCH-05:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCH-06:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCH-07:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCH-08:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCH-09:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCH-10:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCV-01:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCV-02:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCV-03:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCV-04:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCV-05:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCV-06:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCV-07:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCV-08:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCV-09:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MCV-10:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MQV-01:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MQV-02:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MSol-01:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MSol-01:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MSol-01:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MB-01:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MB-02:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MB-03:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MB-04:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MB-05:Current:Setpoint": [0.0, 110.0],
        "A:MI:PS:MB-06:Current:Setpoint": [0.0, 280.0],
        "A:MI:PS:MB-07:Current:Setpoint": [-2.0, 2.0],
        "A:MI:PS:MB-08:Current:Setpoint": [0.0, 110.0],
        "A:MI:PS:MB-10:Current:Setpoint": [0.0, 110.0],
        "A:MI:PS:MB-11:Current:Setpoint": [0.0, 190.0],
    }

    def __init__(self, interface: Interface, params):
        super().__init__(interface, params)

    @staticmethod
    def list_vars():
        # Returns the names of the corrector magnets #
        return [
            "A:MI:PS:MCH-01:Current:Setpoint",
            "A:MI:PS:MCH-03:Current:Setpoint",
            "A:MI:PS:MCH-04:Current:Setpoint",
            "A:MI:PS:MCH-05:Current:Setpoint",
            "A:MI:PS:MCH-06:Current:Setpoint",
            "A:MI:PS:MCH-07:Current:Setpoint",
            "A:MI:PS:MCH-08:Current:Setpoint",
            "A:MI:PS:MCH-09:Current:Setpoint",
            "A:MI:PS:MCH-10:Current:Setpoint",
            "A:MI:PS:MCV-01:Current:Setpoint",
            "A:MI:PS:MCV-02:Current:Setpoint",
            "A:MI:PS:MCV-03:Current:Setpoint",
            "A:MI:PS:MCV-04:Current:Setpoint",
            "A:MI:PS:MCV-05:Current:Setpoint",
            "A:MI:PS:MCV-06:Current:Setpoint",
            "A:MI:PS:MCV-07:Current:Setpoint",
            "A:MI:PS:MCV-08:Current:Setpoint",
            "A:MI:PS:MCV-09:Current:Setpoint",
            "A:MI:PS:MCV-10:Current:Setpoint",
            "A:MI:PS:MQV-01:Current:Setpoint",
            "A:MI:PS:MQV-02:Current:Setpoint",
            "A:MI:PS:MSol-01:Current:Setpoint",
            "A:MI:PS:MSol-01:Current:Setpoint",
            "A:MI:PS:MSol-01:Current:Setpoint",
            "A:MI:PS:MB-01:Current:Setpoint",
            "A:MI:PS:MB-02:Current:Setpoint",
            "A:MI:PS:MB-03:Current:Setpoint",
            "A:MI:PS:MB-04:Current:Setpoint",
            "A:MI:PS:MB-05:Current:Setpoint",
            "A:MI:PS:MB-06:Current:Setpoint",
            "A:MI:PS:MB-07:Current:Setpoint",
            "A:MI:PS:MB-08:Current:Setpoint",
            "A:MI:PS:MB-10:Current:Setpoint",
            "A:MI:PS:MB-11:Current:Setpoint",
        ]

    @staticmethod
    def list_obses():
        # array of the names of all observables
        return OBSERVALBES

    def _get_vrange(self, var):
        # [min, max] of the corrector magnet
        return self.vranges[var]

    def _get_var(self, var):
        return self.interface.get_value(var)

    def _set_var(self, var, x):
        if not self.params["read_only"]:
            self.interface.set_value(var, x)

    def _get_obs(self, obs):
        return self.interface.get_value(obs)

    @staticmethod
    def get_default_params():
        return {
            "waiting_time": 1,
            "read_only": False,
        }

    def vars_changed(self, vars: List[str], values: list):
        time.sleep(self.params["waiting_time"])
