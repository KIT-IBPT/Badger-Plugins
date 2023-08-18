import numpy as np
from badger import environment
from badger.interface import Interface
from Orbit_Correction import feeder 


# Pure number version
def Orbit_Correction(individual1, individual2):
    x1 = individual1[0]
    x2 = individual1[1]
    x3 = individual1[2]
    x4 = individual1[3]
    x5 = individual1[4]
    x6 = individual1[5]
    x7 = individual1[6]
    x8 = individual1[7]
    x9 = individual1[8]
    x10 = individual1[9]
    x11 = individual1[10]
    x12 = individual1[11]
    x13 = individual1[12]
    x14 = individual1[13]
    x15 = individual1[14]
    x16 = individual1[15]
    x17 = individual1[16]
    x18 = individual1[17]
    x19 = individual1[18]
    x20 = individual1[19]
    x21 = individual1[20]
    x22 = individual1[21]
    x23 = individual1[22]
    x24 = individual1[23]
    x25 = individual1[24]
    x26 = individual1[25]
    x27 = individual1[26]
    x28 = individual1[27]
    x29 = individual1[28]
    x30 = individual1[29]
    x31 = individual1[30]
    x32 = individual1[31]
    x33 = individual2[0]
    x34 = individual2[1]
    x35 = individual2[2]
    x36 = individual2[3]
    x37 = individual2[4]
    x38 = individual2[5]
    x39 = individual2[6]
    x40 = individual2[7]
    x41 = individual2[8]
    x42 = individual2[9]
    x43 = individual2[10]
    x44 = individual2[11]
    x45 = individual2[12]
    x46 = individual2[13]
    x47 = individual2[14]
    x48 = individual2[15]
    x49 = individual2[16]
    x50 = individual2[17]
    x51 = individual2[18]
    x52 = individual2[19]
    x53 = individual2[20]
    x54 = individual2[21]
    x55 = individual2[22]
    x56 = individual2[23]
    x57 = individual2[24]
    x58 = individual2[25]
    x59 = individual2[26]
    x60 = individual2[27]
    x61 = individual2[28]
    x62 = individual2[29]
    x63 = individual2[30]
    x64 = individual2[31]
    x65 = individual2[32]
    x66 = individual2[33]
    x67 = individual2[34]
    x68 = individual2[35]
    x69 = individual2[36]
    x70 = individual2[37]
    x71 = individual2[38]
    x72 = individual2[39]
    xi_values = np.array([x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, 
      x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, 
      x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, 
      x31, x32, x33, x34, x35, x36, x37, x38, x39, x40,
      x41, x42, x43, x44, x45, x46, x47, x48, x49, x50,
      x51, x52, x53, x54, x55, x56, x57, x58, x59, x60,
      x61, x62, x63, x64, x65, x66, x67, x68, x69, x70,
      x71, x72])

    objectives = feeder(xi_values)

    return objectives


class Environment(environment.Environment):

    name = 'Orbit_Correction'

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
            'x11': 0,
            'x12': 0,
            'x13': 0,
            'x14': 0,
            'x15': 0,
            'x16': 0,
            'x17': 0,
            'x18': 0,
            'x19': 0,
            'x20': 0,
            'x21': 0,
            'x22': 0,
            'x23': 0,
            'x24': 0,
            'x25': 0,
            'x26': 0,
            'x27': 0,
            'x28': 0,
            'x29': 0,
            'x30': 0,
            'x31': 0,
            'x32': 0,
            'x33': 0,
            'x34': 0,
            'x35': 0,
            'x36': 0,
            'x37': 0,
            'x38': 0,
            'x39': 0,
            'x40': 0,
            'x41': 0,
            'x42': 0,
            'x43': 0,
            'x44': 0,
            'x45': 0,
            'x46': 0,
            'x47': 0,
            'x48': 0,
            'x49': 0,
            'x50': 0,
            'x51': 0,
            'x52': 0,
            'x53': 0,
            'x54': 0,
            'x55': 0,
            'x56': 0,
            'x57': 0,
            'x58': 0,
            'x59': 0,
            'x60': 0,
            'x61': 0,
            'x62': 0,
            'x63': 0,
            'x64': 0,
            'x65': 0,
            'x66': 0,
            'x67': 0,
            'x68': 0,
            'x69': 0,
            'x70': 0,
            'x71': 0,
            'x72': 0,
        }

        self.observations = {
            'y': None,
            'some_array': np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
              11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
              21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
              31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
              41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
              51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
              61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
              71, 72])
        }

    @staticmethod
    def list_vars():
        return ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 
          'x11', 'x12', 'x13', 'x14', 'x15', 'x16', 'x17', 'x18', 'x19', 'x20', 
          'x21', 'x22', 'x23', 'x24', 'x25', 'x26', 'x27', 'x28', 'x29', 'x30', 
          'x31', 'x32', 'x33', 'x34', 'x35', 'x36', 'x37', 'x38', 'x39', 'x40', 
          'x41', 'x42', 'x43', 'x44', 'x45', 'x46', 'x47', 'x48', 'x49', 'x50', 
          'x51', 'x52', 'x53', 'x54', 'x55', 'x56', 'x57', 'x58', 'x59', 'x60', 
          'x61', 'x62', 'x63', 'x64', 'x65', 'x66', 'x67', 'x68', 'x69', 'x70', 
          'x71', 'x72']

    @staticmethod
    def list_obses():
        return ['y', 'some_array']

    @staticmethod
    def get_default_params():
        return None

    def _get_vrange(self, var):
        return [-1000, 1000]

    def _get_var(self, var):
        return self.variables[var]

    def _set_var(self, var, x):
        self.variables[var] = x

        # Filling up the observations
        ind = [self.variables['x1'], self.variables['x2'], self.variables['x3'], 
          self.variables['x4'], self.variables['x5'], self.variables['x6'], 
          self.variables['x7'], self.variables['x8'], self.variables['x9'], self.variables['x10'], 
          self.variables['x11'], self.variables['x12'], self.variables['x13'], 
          self.variables['x14'], self.variables['x15'], self.variables['x16'], 
          self.variables['x17'], self.variables['x18'], self.variables['x19'], self.variables['x20'], 
          self.variables['x21'], self.variables['x22'], self.variables['x23'], 
          self.variables['x24'], self.variables['x25'], self.variables['x26'], 
          self.variables['x27'], self.variables['x28'], self.variables['x29'], self.variables['x30'], 
          self.variables['x31'], self.variables['x32'], self.variables['x33'], 
          self.variables['x34'], self.variables['x35'], self.variables['x36'], 
          self.variables['x37'], self.variables['x38'], self.variables['x39'], self.variables['x40'], 
          self.variables['x41'], self.variables['x42'], self.variables['x43'], 
          self.variables['x44'], self.variables['x45'], self.variables['x46'], 
          self.variables['x47'], self.variables['x48'], self.variables['x49'], self.variables['x50'],
          self.variables['x51'], self.variables['x25'], self.variables['x53'], 
          self.variables['x54'], self.variables['x55'], self.variables['x56'], 
          self.variables['x57'], self.variables['x58'], self.variables['x59'], self.variables['x60'],  
          self.variables['x61'], self.variables['x62'], self.variables['x63'], 
          self.variables['x64'], self.variables['x65'], self.variables['x66'], 
          self.variables['x67'], self.variables['x68'], self.variables['x69'], self.variables['x70'], 
          self.variables['x71'], self.variables['x72']]
        
        objectives = Orbit_Correction(ind)
        self.observations['y'] = objectives

    def _get_obs(self, obs):
        return self.observations[obs]