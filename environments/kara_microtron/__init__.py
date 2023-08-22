import numpy as np
from badger import environment
from badger.interface import Interface


# Pure number version
def Orbit_Correction(signals):

    # array containing the beam currents. Cannot be changed because they are observables. #
    bc_values = np.array(signals)

    # still need to enter how the objectives are calculated #
    objectives = 0

    return objectives

# array containing names of the beam currents. Used to communicate with SoftIOC and epics. #
BC_NAMES = [

        'A:MI:DTACQChannel:BeamCurrent-EGun:Mean',
        'A:MI:DTACQChannel:BeamCurrent-02:Mean',
        'A:MI:DTACQChannel:BeamCurrent-03:Mean',
        'A:MI:DTACQChannel:BeamCurrent-04:Mean',
        'A:MI:DTACQChannel:BeamCurrent-05:Mean',
        'A:MI:DTACQChannel:BeamCurrent-06:Mean',
        'A:MI:DTACQChannel:BeamCurrent-07:Mean',
        'A:MI:DTACQChannel:BeamCurrent-08:Mean',

    ]

# environment containing all the process variables and objective functions for the KARA Microtron #
class Environment(environment.Environment):
    name = 'Kara_Microtron'



    def __init__(self, interface: Interface, params):
        super().__init__(interface, params)


        # array containing names of the corrector magnets initialized to their respective use ranges. Used to communicate with SoftIOC and epics. #

        self.variables = {

            'A:MI:PS:MCH-01:Current:Setpoint': [-2.0, 2.0],
            'A:MI:PS:MCH-03:Current:Setpoint': [-2.0, 2.0],
            'A:MI:PS:MCH-04:Current:Setpoint': [-2.0, 2.0],
            'A:MI:PS:MCH-05:Current:Setpoint': [-2.0, 2.0],
            'A:MI:PS:MCH-06:Current:Setpoint': [-2.0, 2.0],
            'A:MI:PS:MCH-07:Current:Setpoint': [-2.0, 2.0],
            'A:MI:PS:MCH-08:Current:Setpoint': [-2.0, 2.0],
            'A:MI:PS:MCH-09:Current:Setpoint': [-2.0, 2.0],
            'A:MI:PS:MCH-10:Current:Setpoint': [-2.0, 2.0],
            'A:MI:PS:MCV-01:Current:Setpoint': [-2.0, 2.0],
            'A:MI:PS:MCV-02:Current:Setpoint': [-2.0, 2.0],
            'A:MI:PS:MCV-03:Current:Setpoint': [-2.0, 2.0],
            'A:MI:PS:MCV-04:Current:Setpoint': [-2.0, 2.0],
            'A:MI:PS:MCV-05:Current:Setpoint': [-2.0, 2.0],
            'A:MI:PS:MCV-06:Current:Setpoint': [-2.0, 2.0],
            'A:MI:PS:MCV-07:Current:Setpoint': [-2.0, 2.0],
            'A:MI:PS:MCV-08:Current:Setpoint': [-2.0, 2.0],
            'A:MI:PS:MCV-09:Current:Setpoint': [-2.0, 2.0],
            'A:MI:PS:MCV-10:Current:Setpoint': [-2.0, 2.0],
            'A:MI:PS:MQV-01:Current:Setpoint': [-2.0, 2.0],
            'A:MI:PS:MQV-02:Current:Setpoint': [-2.0, 2.0],
            'A:MI:PS:MSol-01:Current:Setpoint': [-2.0, 2.0],
            'A:MI:PS:MSol-01:Current:Setpoint': [-2.0, 2.0],
            'A:MI:PS:MSol-01:Current:Setpoint': [-2.0, 2.0],
            'A:MI:PS:MB-01:Current:Setpoint': [-2.0, 2.0],
            'A:MI:PS:MB-02:Current:Setpoint': [-2.0, 2.0],
            'A:MI:PS:MB-03:Current:Setpoint': [-2.0, 2.0],
            'A:MI:PS:MB-04:Current:Setpoint': [-2.0, 2.0],
            'A:MI:PS:MB-05:Current:Setpoint': [0.0, 110.0],
            'A:MI:PS:MB-06:Current:Setpoint': [0.0, 280.0],
            'A:MI:PS:MB-07:Current:Setpoint': [-2.0, 2.0],
            'A:MI:PS:MB-08:Current:Setpoint': [0.0, 110.0],
            'A:MI:PS:MB-10:Current:Setpoint': [0.0, 110.0],
            'A:MI:PS:MB-11:Current:Setpoint': [0.0, 190.0]

        }


    @staticmethod
    def list_vars():
        # Returns the names of the corrector magnets #
        return [

            'A:MI:PS:MCH-01:Current:Setpoint',
            'A:MI:PS:MCH-03:Current:Setpoint',
            'A:MI:PS:MCH-04:Current:Setpoint',
            'A:MI:PS:MCH-05:Current:Setpoint',
            'A:MI:PS:MCH-06:Current:Setpoint',
            'A:MI:PS:MCH-07:Current:Setpoint',
            'A:MI:PS:MCH-08:Current:Setpoint',
            'A:MI:PS:MCH-09:Current:Setpoint',
            'A:MI:PS:MCH-10:Current:Setpoint',
            'A:MI:PS:MCV-01:Current:Setpoint',
            'A:MI:PS:MCV-02:Current:Setpoint',
            'A:MI:PS:MCV-03:Current:Setpoint',
            'A:MI:PS:MCV-04:Current:Setpoint',
            'A:MI:PS:MCV-05:Current:Setpoint',
            'A:MI:PS:MCV-06:Current:Setpoint',
            'A:MI:PS:MCV-07:Current:Setpoint',
            'A:MI:PS:MCV-08:Current:Setpoint',
            'A:MI:PS:MCV-09:Current:Setpoint',
            'A:MI:PS:MCV-10:Current:Setpoint',
            'A:MI:PS:MQV-01:Current:Setpoint',
            'A:MI:PS:MQV-02:Current:Setpoint',
            'A:MI:PS:MSol-01:Current:Setpoint',
            'A:MI:PS:MSol-01:Current:Setpoint',
            'A:MI:PS:MSol-01:Current:Setpoint',
            'A:MI:PS:MB-01:Current:Setpoint',
            'A:MI:PS:MB-02:Current:Setpoint',
            'A:MI:PS:MB-03:Current:Setpoint',
            'A:MI:PS:MB-04:Current:Setpoint',
            'A:MI:PS:MB-05:Current:Setpoint',
            'A:MI:PS:MB-06:Current:Setpoint',
            'A:MI:PS:MB-07:Current:Setpoint',
            'A:MI:PS:MB-08:Current:Setpoint',
            'A:MI:PS:MB-10:Current:Setpoint',
            'A:MI:PS:MB-11:Current:Setpoint'
            
        ]
    
    @staticmethod
    def list_obses():
        # array of the names of all observables #
        return  ["name of observable"] + BC_NAMES

    @staticmethod
    def get_default_params():
        return None

    def _get_vrange(self, var):
        # maximum and minimum strengths of a magnet #
        self.variables[var]

    def _get_var(self, var):
        # TODO: update pv limits every time?
        return self.interface.get_value(var)

    def _set_var(self, var, x):
        self.interface.set_value(var, x)


    def _get_obs(self, obs):
        return self.interface.get_value(obs)