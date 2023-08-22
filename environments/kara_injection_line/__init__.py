import numpy as np
from badger import environment
from badger.interface import Interface


# array containing names of the beam currents. Used to communicate with SoftIOC and epics. #
BEAM_CURRENT = [ 'A:BO:DTACQChannel:BeamCurrent:Max', ]



# environment containing all the process variables and objective functions for the KARA Microtron #
class Environment(environment.Environment):
    name = 'Kara_Injection_Line'



    def __init__(self, interface: Interface, params):
        super().__init__(interface, params)


        # array containing names of the corrector magnets initialized to their respective use ranges. Used to communicate with SoftIOC and epics. #

        self.variables = {

            'A:MI:PS:MB-11:Current:Setpoint': [0.0, 190.0],
            'A:IL:PS:MCH-01:Current:Setpoint': [-2.0, 2.0],
            'A:IL:PS:MCH-02:Current:Setpoint': [-2.0, 2.0],
            'A:IL:PS:MCH-03:Current:Setpoint': [-2.0, 2.0],
            'A:IL:PS:MCH-04:Current:Setpoint': [-2.0, 2.0],
            'A:IL:PS:MCV-01:Current:Setpoint': [-2.0, 2.0],
            'A:IL:PS:MCV-02:Current:Setpoint': [-2.0, 2.0],
            'A:IL:PS:MCV-03:Current:Setpoint': [-2.0, 2.0],
            'A:IL:PS:MCV-04:Current:Setpoint': [-2.0, 2.0],
            'A:IL:PS:MQ-01:Current:Setpoint': [0.0, 8.0],
            'A:IL:PS:MQ-02:Current:Setpoint': [0.0, 8.0],
            'A:IL:PS:MQ-03:Current:Setpoint': [0.0, 8.0],
            'A:IL:PS:MQ-04:Current:Setpoint': [0.0, 8.0],
            'A:IL:PS:MQ-05:Current:Setpoint': [0.0, 8.0],
            'A:IL:PS:MB-01:Current:Setpoint': [0.0, 95.0],
            # 'A:IL:PS:MB-02:Current:Setpoint': [0.0, 95.0], not in KARA registry

        }


    @staticmethod
    def list_vars():
        # Returns the names of the corrector magnets #
        return [

            'A:MI:PS:MB-11:Current:Setpoint',
            'A:IL:PS:MCH-01:Current:Setpoint',
            'A:IL:PS:MCH-02:Current:Setpoint',
            'A:IL:PS:MCH-03:Current:Setpoint',
            'A:IL:PS:MCH-04:Current:Setpoint',
            'A:IL:PS:MCV-01:Current:Setpoint',
            'A:IL:PS:MCV-02:Current:Setpoint',
            'A:IL:PS:MCV-03:Current:Setpoint',
            'A:IL:PS:MCV-04:Current:Setpoint',
            'A:IL:PS:MQ-01:Current:Setpoint',
            'A:IL:PS:MQ-02:Current:Setpoint',
            'A:IL:PS:MQ-03:Current:Setpoint',
            'A:IL:PS:MQ-04:Current:Setpoint',
            'A:IL:PS:MQ-05:Current:Setpoint',
            'A:IL:PS:MB-01:Current:Setpoint',
            # 'A:IL:PS:MB-02:Current:Setpoint': [0.0, 95.0], not in KARA registry
            
        ]
    
    @staticmethod
    def list_obses():
        # array of the names of all observables #
        return BEAM_CURRENT

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