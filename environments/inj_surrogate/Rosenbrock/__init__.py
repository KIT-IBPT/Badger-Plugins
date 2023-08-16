import numpy as np
from badger import environment
from badger.interface import Interface


# Pure number version
def Rosenbrock(individual):
    x1 = individual[0]
    x2 = individual[1]
    x3 = individual[2]
    x4 = individual[3]
    x5 = individual[4]
    x6 = individual[5]
    x7 = individual[6]
    x8 = individual[7]
    x9 = individual[8]
    x10 = individual[9]
    xi_values = np.array([x1, x2, x3, x4, x5, x6, x7, x8, x9, x10])
    
    objectives = 0
    for i in range(10):
        objectives += (100 * (xi_values[i] - xi_values[i]**2)**2 + (xi_values[i] - 1)**2)
    return objectives


class Environment(environment.Environment):

    name = 'Rosenbrock'

    def __init__(self, interface: Interface, params):
        super().__init__(interface, params)

        self.variables = {
            'x1': 0,
            'x2': 0,
            'x3': 0,
            'x4': 0,
            'x5': 0,
            'x6': 0,
            'x7': 0,
            'x8': 0,
            'x9': 0,
            'x10': 0,
        }
        self.observations = {
            'y': None,
            'some_array': np.array([1, 2, 3]),
        }

    @staticmethod
    def list_vars():
        return ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10']

    @staticmethod
    def list_obses():
        return ['y', 'some_array']

    @staticmethod
    def get_default_params():
        return None

    def _get_vrange(self, var):
        return [-2.048, 2.048]

    def _get_var(self, var):
        return self.variables[var]

    def _set_var(self, var, x):
        self.variables[var] = x

        # Filling up the observations
        ind = [self.variables['x1'], self.variables['x2'], self.variables['x3'], 
          self.variables['x4'], self.variables['x5'], self.variables['x6'], 
          self.variables['x7'], self.variables['x8'], self.variables['x9'], self.variables['x10']]
        objectives = Rosenbrock(ind)
        self.observations['y'] = objectives[0]

    def _get_obs(self, obs):
        return self.observations[obs]
