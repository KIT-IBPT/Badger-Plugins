import numpy as np
from badger import environment
from badger.interface import Interface


# Pure number version
def Orbit_Correction(monitors):

    # array containing the beam monitors. Cannot be changed because they are observables. #
    bpm_values = np.array(monitors)

    # mean square error #
    mse = 0
    # loss 1 function #
    l1 = 0

    mse = np.mean((bpm_values - 0) ** 2)
    l1 = np.mean(np.abs(bpm_values - 0))

    objectives = (mse, l1)

    return objectives

# array containing names of the beam monitors. Used to communicate with SoftIOC and epics. #
BPM_NAMES = [
        'DEBUG:A:SR-S1:BPM:01:SA:X',
        'DEBUG:A:SR-S1:BPM:02:SA:X',
        'DEBUG:A:SR-S1:BPM:03:SA:X',
        'DEBUG:A:SR-S1:BPM:04:SA:X',
        'DEBUG:A:SR-S1:BPM:05:SA:X',
        'DEBUG:A:SR-S1:BPM:06:SA:X',
        'DEBUG:A:SR-S1:BPM:07:SA:X',
        'DEBUG:A:SR-S1:BPM:08:SA:X',
        'DEBUG:A:SR-S1:BPM:09:SA:X',
        'DEBUG:A:SR-S1:BPM:10:SA:X',
        'DEBUG:A:SR-S2:BPM:01:SA:X',
        'DEBUG:A:SR-S2:BPM:02:SA:X',
        'DEBUG:A:SR-S2:BPM:03:SA:X',
        'DEBUG:A:SR-S2:BPM:04:SA:X',
        'DEBUG:A:SR-S2:BPM:05:SA:X',
        'DEBUG:A:SR-S2:BPM:06:SA:X',
        'DEBUG:A:SR-S2:BPM:07:SA:X',
        'DEBUG:A:SR-S2:BPM:08:SA:X',
        'DEBUG:A:SR-S2:BPM:09:SA:X',
        'DEBUG:A:SR-S2:BPM:10:SA:X',
        'DEBUG:A:SR-S3:BPM:01:SA:X',
        'DEBUG:A:SR-S3:BPM:02:SA:X',
        'DEBUG:A:SR-S3:BPM:03:SA:X',
        'DEBUG:A:SR-S3:BPM:04:SA:X',
        'DEBUG:A:SR-S3:BPM:05:SA:X',
        'DEBUG:A:SR-S3:BPM:06:SA:X',
        'DEBUG:A:SR-S3:BPM:07:SA:X',
        'DEBUG:A:SR-S3:BPM:08:SA:X',
        'DEBUG:A:SR-S3:BPM:09:SA:X',
        'DEBUG:A:SR-S3:BPM:10:SA:X',
        'DEBUG:A:SR-S4:BPM:01:SA:X',
        'DEBUG:A:SR-S4:BPM:03:SA:X',
        'DEBUG:A:SR-S4:BPM:04:SA:X',
        'DEBUG:A:SR-S4:BPM:05:SA:X',
        'DEBUG:A:SR-S4:BPM:06:SA:X',
        'DEBUG:A:SR-S4:BPM:07:SA:X',
        'DEBUG:A:SR-S4:BPM:08:SA:X',
        'DEBUG:A:SR-S4:BPM:09:SA:X',
        'DEBUG:A:SR-S4:BPM:10:SA:X'
    ]

class Environment(environment.Environment):
    name = 'Orbit_Correction'



    def __init__(self, interface: Interface, params):
        super().__init__(interface, params)


        # array containing names of the corrector magnets initialized to 0. Used to communicate with SoftIOC and epics. #

        self.variables = { 

            'DEBUG:A:SR-S1:PS:MCH-01:Current:Setpoint': 0,
            'DEBUG:A:SR-S1:PS:MCH-02:Current:Setpoint': 0,
            'DEBUG:A:SR-S1:PS:MCH-03:Current:Setpoint': 0,
            'DEBUG:A:SR-S1:PS:MCH-04:Current:Setpoint': 0,
            'DEBUG:A:SR-S1:PS:MCH-06:Current:Setpoint': 0,
            'DEBUG:A:SR-S1:PS:MCH-07:Current:Setpoint': 0,
            'DEBUG:A:SR-S1:PS:MCH-08:Current:Setpoint': 0,
            'DEBUG:A:SR-S2:PS:MCH-01:Current:Setpoint': 0,
            'DEBUG:A:SR-S2:PS:MCH-02:Current:Setpoint': 0,
            'DEBUG:A:SR-S2:PS:MCH-03:Current:Setpoint': 0,
            'DEBUG:A:SR-S2:PS:MCH-04:Current:Setpoint': 0,
            'DEBUG:A:SR-S2:PS:MCH-06:Current:Setpoint': 0,
            'DEBUG:A:SR-S2:PS:MCH-07:Current:Setpoint': 0,
            'DEBUG:A:SR-S2:PS:MCH-08:Current:Setpoint': 0,
            'DEBUG:A:SR-S3:PS:MCH-01:Current:Setpoint': 0,
            'DEBUG:A:SR-S3:PS:MCH-02:Current:Setpoint': 0,
            'DEBUG:A:SR-S3:PS:MCH-03:Current:Setpoint': 0,
            'DEBUG:A:SR-S3:PS:MCH-04:Current:Setpoint': 0,
            'DEBUG:A:SR-S3:PS:MCH-06:Current:Setpoint': 0,
            'DEBUG:A:SR-S3:PS:MCH-07:Current:Setpoint': 0,
            'DEBUG:A:SR-S3:PS:MCH-08:Current:Setpoint': 0,
            'DEBUG:A:SR-S4:PS:MCH-01:Current:Setpoint': 0,
            'DEBUG:A:SR-S4:PS:MCH-02:Current:Setpoint': 0,
            'DEBUG:A:SR-S4:PS:MCH-03:Current:Setpoint': 0,
            'DEBUG:A:SR-S4:PS:MCH-04:Current:Setpoint': 0,
            'DEBUG:A:SR-S4:PS:MCH-06:Current:Setpoint': 0,
            'DEBUG:A:SR-S4:PS:MCH-07:Current:Setpoint': 0,
            'DEBUG:A:SR-S4:PS:MCH-08:Current:Setpoint': 0,

        }

        # Set the first 2 correctors to be non-zero for environment 2
        self._set_var('DEBUG:A:SR-S1:PS:MCH-01:Current:Setpoint', 0.3)
        self._set_var('DEBUG:A:SR-S1:PS:MCH-02:Current:Setpoint', 0.3)

    @staticmethod
    def list_vars():
        # Returns the values of the corrector magnets #
        return [
            'DEBUG:A:SR-S1:PS:MCH-01:Current:Setpoint',
            'DEBUG:A:SR-S1:PS:MCH-02:Current:Setpoint',
            'DEBUG:A:SR-S1:PS:MCH-03:Current:Setpoint',
            'DEBUG:A:SR-S1:PS:MCH-04:Current:Setpoint',
            'DEBUG:A:SR-S1:PS:MCH-06:Current:Setpoint',
            'DEBUG:A:SR-S1:PS:MCH-07:Current:Setpoint',
            'DEBUG:A:SR-S1:PS:MCH-08:Current:Setpoint',
            'DEBUG:A:SR-S2:PS:MCH-01:Current:Setpoint',
            'DEBUG:A:SR-S2:PS:MCH-02:Current:Setpoint',
            'DEBUG:A:SR-S2:PS:MCH-03:Current:Setpoint',
            'DEBUG:A:SR-S2:PS:MCH-04:Current:Setpoint',
            'DEBUG:A:SR-S2:PS:MCH-06:Current:Setpoint',
            'DEBUG:A:SR-S2:PS:MCH-07:Current:Setpoint',
            'DEBUG:A:SR-S2:PS:MCH-08:Current:Setpoint',
            'DEBUG:A:SR-S3:PS:MCH-01:Current:Setpoint',
            'DEBUG:A:SR-S3:PS:MCH-02:Current:Setpoint',
            'DEBUG:A:SR-S3:PS:MCH-03:Current:Setpoint',
            'DEBUG:A:SR-S3:PS:MCH-04:Current:Setpoint',
            'DEBUG:A:SR-S3:PS:MCH-06:Current:Setpoint',
            'DEBUG:A:SR-S3:PS:MCH-07:Current:Setpoint',
            'DEBUG:A:SR-S3:PS:MCH-08:Current:Setpoint',
            'DEBUG:A:SR-S4:PS:MCH-01:Current:Setpoint',
            'DEBUG:A:SR-S4:PS:MCH-02:Current:Setpoint',
            'DEBUG:A:SR-S4:PS:MCH-03:Current:Setpoint',
            'DEBUG:A:SR-S4:PS:MCH-04:Current:Setpoint',
            'DEBUG:A:SR-S4:PS:MCH-06:Current:Setpoint',
            'DEBUG:A:SR-S4:PS:MCH-07:Current:Setpoint',
            'DEBUG:A:SR-S4:PS:MCH-08:Current:Setpoint'
        ]
    
    @staticmethod
    def list_obses():
        # array of all observables #
        return  ["mse", "l1"] + BPM_NAMES

    @staticmethod
    def get_default_params():
        return None

    def _get_vrange(self, var):
        # maximum and minimum strengths of the magnets #
        return [-1, 1]

    def _get_var(self, var):
        # TODO: update pv limits every time?
        return self.interface.get_value(var)

    def _set_var(self, var, x):
        self.interface.set_value(var, x)


    def _get_obs(self, obs):
        
        if obs == "mse":
            monitors = [self.interface.get_value(obs) for obs in BPM_NAMES]
            return Orbit_Correction(monitors)[0]
        if obs == "l1":
            monitors = [self.interface.get_value(obs) for obs in BPM_NAMES]
            return Orbit_Correction(monitors)[1]
        else:
            return self.interface.get_value(obs)