from typing import Union

import numpy as np
from badger import environment
from badger.interface import Interface


# Pure number version
def calculate_objective(
    bpm_values: Union[list, np.ndarray], loss_mode: str = "mse"
) -> float:
    # array containing the beam monitors. Cannot be changed because they are observables. #
    bpm_values = np.array(bpm_values)

    if loss_mode == "mse":
        loss = np.mean((bpm_values - 0) ** 2)
    elif loss_mode == "mae":
        loss = np.mean(np.abs(bpm_values - 0))
    else:
        raise ValueError("Invalid loss mode")
    return loss


# array containing names of the beam monitors. Used to communicate with SoftIOC and epics. #
CORRECTOR_NAMES = [
    "DEBUG:A:SR-S1:PS:MCH-01:Current:Setpoint",
    "DEBUG:A:SR-S1:PS:MCH-02:Current:Setpoint",
    "DEBUG:A:SR-S1:PS:MCH-03:Current:Setpoint",
    "DEBUG:A:SR-S1:PS:MCH-04:Current:Setpoint",
    "DEBUG:A:SR-S1:PS:MCH-06:Current:Setpoint",
    "DEBUG:A:SR-S1:PS:MCH-07:Current:Setpoint",
    "DEBUG:A:SR-S1:PS:MCH-08:Current:Setpoint",
    "DEBUG:A:SR-S2:PS:MCH-01:Current:Setpoint",
    "DEBUG:A:SR-S2:PS:MCH-02:Current:Setpoint",
    "DEBUG:A:SR-S2:PS:MCH-03:Current:Setpoint",
    "DEBUG:A:SR-S2:PS:MCH-04:Current:Setpoint",
    "DEBUG:A:SR-S2:PS:MCH-06:Current:Setpoint",
    "DEBUG:A:SR-S2:PS:MCH-07:Current:Setpoint",
    "DEBUG:A:SR-S2:PS:MCH-08:Current:Setpoint",
    "DEBUG:A:SR-S3:PS:MCH-01:Current:Setpoint",
    "DEBUG:A:SR-S3:PS:MCH-02:Current:Setpoint",
    "DEBUG:A:SR-S3:PS:MCH-03:Current:Setpoint",
    "DEBUG:A:SR-S3:PS:MCH-04:Current:Setpoint",
    "DEBUG:A:SR-S3:PS:MCH-06:Current:Setpoint",
    "DEBUG:A:SR-S3:PS:MCH-07:Current:Setpoint",
    "DEBUG:A:SR-S3:PS:MCH-08:Current:Setpoint",
    "DEBUG:A:SR-S4:PS:MCH-01:Current:Setpoint",
    "DEBUG:A:SR-S4:PS:MCH-02:Current:Setpoint",
    "DEBUG:A:SR-S4:PS:MCH-03:Current:Setpoint",
    "DEBUG:A:SR-S4:PS:MCH-04:Current:Setpoint",
    "DEBUG:A:SR-S4:PS:MCH-06:Current:Setpoint",
    "DEBUG:A:SR-S4:PS:MCH-07:Current:Setpoint",
    "DEBUG:A:SR-S4:PS:MCH-08:Current:Setpoint",
]

BPM_NAMES = [
    "DEBUG:A:SR-S1:BPM:01:SA:X",
    "DEBUG:A:SR-S1:BPM:02:SA:X",
    "DEBUG:A:SR-S1:BPM:03:SA:X",
    "DEBUG:A:SR-S1:BPM:04:SA:X",
    "DEBUG:A:SR-S1:BPM:05:SA:X",
    "DEBUG:A:SR-S1:BPM:06:SA:X",
    "DEBUG:A:SR-S1:BPM:07:SA:X",
    "DEBUG:A:SR-S1:BPM:08:SA:X",
    "DEBUG:A:SR-S1:BPM:09:SA:X",
    "DEBUG:A:SR-S1:BPM:10:SA:X",
    "DEBUG:A:SR-S2:BPM:01:SA:X",
    "DEBUG:A:SR-S2:BPM:02:SA:X",
    "DEBUG:A:SR-S2:BPM:03:SA:X",
    "DEBUG:A:SR-S2:BPM:04:SA:X",
    "DEBUG:A:SR-S2:BPM:05:SA:X",
    "DEBUG:A:SR-S2:BPM:06:SA:X",
    "DEBUG:A:SR-S2:BPM:07:SA:X",
    "DEBUG:A:SR-S2:BPM:08:SA:X",
    "DEBUG:A:SR-S2:BPM:09:SA:X",
    "DEBUG:A:SR-S2:BPM:10:SA:X",
    "DEBUG:A:SR-S3:BPM:01:SA:X",
    "DEBUG:A:SR-S3:BPM:02:SA:X",
    "DEBUG:A:SR-S3:BPM:03:SA:X",
    "DEBUG:A:SR-S3:BPM:04:SA:X",
    "DEBUG:A:SR-S3:BPM:05:SA:X",
    "DEBUG:A:SR-S3:BPM:06:SA:X",
    "DEBUG:A:SR-S3:BPM:07:SA:X",
    "DEBUG:A:SR-S3:BPM:08:SA:X",
    "DEBUG:A:SR-S3:BPM:09:SA:X",
    "DEBUG:A:SR-S3:BPM:10:SA:X",
    "DEBUG:A:SR-S4:BPM:01:SA:X",
    "DEBUG:A:SR-S4:BPM:03:SA:X",
    "DEBUG:A:SR-S4:BPM:04:SA:X",
    "DEBUG:A:SR-S4:BPM:05:SA:X",
    "DEBUG:A:SR-S4:BPM:06:SA:X",
    "DEBUG:A:SR-S4:BPM:07:SA:X",
    "DEBUG:A:SR-S4:BPM:08:SA:X",
    "DEBUG:A:SR-S4:BPM:09:SA:X",
    "DEBUG:A:SR-S4:BPM:10:SA:X",
]


class Environment(environment.Environment):
    name = "Orbit_Correction"

    def __init__(self, interface: Interface, params):
        super().__init__(interface, params)

        # Set the random seed
        np.random.seed(self.params["random_seed"])

        # Set the first n correctors to be non-zero
        for i in range(self.params["n_correctors"]):
            self._set_var(CORRECTOR_NAMES[i], np.random.uniform(-0.5, 0.5))

    @staticmethod
    def list_vars():
        # Returns the values of the corrector magnets #
        return CORRECTOR_NAMES

    @staticmethod
    def list_obses():
        # array of all observables #
        return ["mse", "mae"] + BPM_NAMES

    @staticmethod
    def get_default_params():
        param = {
            "random_seed": None,
            "n_correctors": 2,
        }
        return param

    def _get_vrange(self, var):
        # maximum and minimum strengths of the magnets #
        return [-1, 1]

    def _get_var(self, var):
        # TODO: update pv limits every time?
        return self.interface.get_value(var)

    def _set_var(self, var, x):
        self.interface.set_value(var, x)

    def _get_obs(self, obs):
        bpm_values = [self.interface.get_value(obs) for obs in BPM_NAMES]
        if obs == "mse" or obs == "mae":
            return calculate_objective(bpm_values, obs)
        else:
            return self.interface.get_value(obs)
