import numpy as np
from badger import environment
from badger.interface import Interface
from typing import List
import time


# array containing names of the beam currents. Used to communicate with SoftIOC and epics. #
OUTPUT_NAMES = [

        'A:SR:Model:Ocelot-01:Offline:Tune:X',
        'A:SR:Model:Ocelot-01:Offline:Tune:Y',
        'A:SR:Model:Ocelot-01:Offline:Chromaticity:X',
        'A:SR:Model:Ocelot-01:Offline:Chromaticity:Y',
        'A:SR:Model:Ocelot-01:Offline:AlphaC',
        'A:SR:Model:Ocelot-01:Offline:SimulationDuration',

    ]

# environment containing all the process variables and objective functions for the KARA Ocelot #
class Environment(environment.Environment):
    name = 'Kara_Ocelot'



    def __init__(self, interface: Interface, params):
        super().__init__(interface, params)


        # array containing names of the corrector magnets initialized to their respective use ranges. Used to communicate with SoftIOC and epics. #

        self.variables = {

            'A:SR:Model:Ocelot-01:Offline:BEND:CURRENT': [0.0, 1000.0],
            'A:SR:Model:Ocelot-01:Offline:Q1:CURRENT': [0.0, 1000.0],
            'A:SR:Model:Ocelot-01:Offline:Q2:CURRENT': [0.0, 1000.0],
            'A:SR:Model:Ocelot-01:Offline:Q3:CURRENT': [0.0, 1000.0],
            'A:SR:Model:Ocelot-01:Offline:Q4:CURRENT': [0.0, 1000.0],
            'A:SR:Model:Ocelot-01:Offline:Q5:CURRENT': [0.0, 1000.0],
            'A:SR:Model:Ocelot-01:Offline:SH:CURRENT': [0.0, 1000.0],
            'A:SR:Model:Ocelot-01:Offline:SV1:CURRENT': [0.0, 1000.0],
            'A:SR:Model:Ocelot-01:Offline:SV2:CURRENT': [0.0, 1000.0],

        }


    @staticmethod
    def list_vars():
        # Returns the names of the corrector magnets #
        return [

            'A:SR:Model:Ocelot-01:Offline:BEND:CURRENT',
            'A:SR:Model:Ocelot-01:Offline:Q1:CURRENT',
            'A:SR:Model:Ocelot-01:Offline:Q2:CURRENT',
            'A:SR:Model:Ocelot-01:Offline:Q3:CURRENT',
            'A:SR:Model:Ocelot-01:Offline:Q4:CURRENT',
            'A:SR:Model:Ocelot-01:Offline:Q5:CURRENT',
            'A:SR:Model:Ocelot-01:Offline:SH:CURRENT',
            'A:SR:Model:Ocelot-01:Offline:SV1:CURRENT',
            'A:SR:Model:Ocelot-01:Offline:SV2:CURRENT',
            
        ]
    
    @staticmethod
    def list_obses():
        # array of the names of all observables #
        return  OUTPUT_NAMES

    def _get_vrange(self, var):
        # maximum and minimum strengths of a magnet #
        return self.variables[var]

    def _get_var(self, var):
        # TODO: update pv limits every time?
        return self.interface.get_value(var)

    def _set_var(self, var, x):
        self.interface.set_value(var, x)


    def _get_obs(self, obs):
        return self.interface.get_value(obs)

    @staticmethod
    def get_default_params():
        return {
            'waiting_time': 1,
        }
    
    def vars_changed(self, vars: List[str], values: list):
        time.sleep(self.params["waiting_time"])