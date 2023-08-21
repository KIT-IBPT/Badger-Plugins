import numpy as np
from badger import environment
from badger.interface import Interface


# Pure number version
def Orbit_Correction(magnets, monitors):
    x1 = magnets[0]
    x2 = magnets[1]
    x3 = magnets[2]
    x4 = magnets[3]
    x5 = magnets[4]
    x6 = magnets[5]
    x7 = magnets[6]
    x8 = magnets[7]
    x9 = magnets[8]
    x10 = magnets[9]
    x11 = magnets[10]
    x12 = magnets[11]
    x13 = magnets[12]
    x14 = magnets[13]
    x15 = magnets[14]
    x16 = magnets[15]
    x17 = magnets[16]
    x18 = magnets[17]
    x19 = magnets[18]
    x20 = magnets[19]
    x21 = magnets[20]
    x22 = magnets[21]
    x23 = magnets[22]
    x24 = magnets[23]
    x25 = magnets[24]
    x26 = magnets[25]
    x27 = magnets[26]
    x28 = magnets[27]
    x29 = magnets[28]
    x30 = magnets[29]
    x31 = magnets[30]
    x32 = magnets[31]
    x33 = monitors[0]
    x34 = monitors[1]
    x35 = monitors[2]
    x36 = monitors[3]
    x37 = monitors[4]
    x38 = monitors[5]
    x39 = monitors[6]
    x40 = monitors[7]
    x41 = monitors[8]
    x42 = monitors[9]
    x43 = monitors[10]
    x44 = monitors[11]
    x45 = monitors[12]
    x46 = monitors[13]
    x47 = monitors[14]
    x48 = monitors[15]
    x49 = monitors[16]
    x50 = monitors[17]
    x51 = monitors[18]
    x52 = monitors[19]
    x53 = monitors[20]
    x54 = monitors[21]
    x55 = monitors[22]
    x56 = monitors[23]
    x57 = monitors[24]
    x58 = monitors[25]
    x59 = monitors[26]
    x60 = monitors[27]
    x61 = monitors[28]
    x62 = monitors[29]
    x63 = monitors[30]
    x64 = monitors[31]
    x65 = monitors[32]
    x66 = monitors[33]
    x67 = monitors[34]
    x68 = monitors[35]
    x69 = monitors[36]
    x70 = monitors[37]
    x71 = monitors[38]
    x72 = monitors[39]
    xi_values = np.array([x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, 
      x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, 
      x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, 
      x31, x32, x33, x34, x35, x36, x37, x38, x39, x40,
      x41, x42, x43, x44, x45, x46, x47, x48, x49, x50,
      x51, x52, x53, x54, x55, x56, x57, x58, x59, x60,
      x61, x62, x63, x64, x65, x66, x67, x68, x69, x70,
      x71, x72])

    mse = 0
    l1l = 0
    for i in range(72):
        mse += (xi_values[i]) ** 2
        l1l += np.abs(xi_values[i])
    mse /= 72
    objectives = (mse, l1l)

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
        return [-1, 1]

    def _get_var(self, var):
        return self.variables[var]

    def _set_var(self, var, x):
        self.variables[var] = x

        # Filling up the observations
        mags = [self.variables['x1'], self.variables['x2'], self.variables['x3'], 
          self.variables['x4'], self.variables['x5'], self.variables['x6'], 
          self.variables['x7'], self.variables['x8'], self.variables['x9'], self.variables['x10'], 
          self.variables['x11'], self.variables['x12'], self.variables['x13'], 
          self.variables['x14'], self.variables['x15'], self.variables['x16'], 
          self.variables['x17'], self.variables['x18'], self.variables['x19'], self.variables['x20'], 
          self.variables['x21'], self.variables['x22'], self.variables['x23'], 
          self.variables['x24'], self.variables['x25'], self.variables['x26'], 
          self.variables['x27'], self.variables['x28'], self.variables['x29'], self.variables['x30'], 
          self.variables['x31']]
        
        cors = [self.variables['x32'], self.variables['x33'], 
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