from environments.Orbit_Correction import Environment
import numpy as np

def test_orbit_environment():
    orbit_env = Environment(None, {})

    variables = orbit_env.variables

    # make sure variables start out as 0 #
    for key in variables.keys():
        assert variables[key] == 0 

    orbit_env._set_var("x1",1)
    orbit_env._set_var("x2",-0.4)

    assert abs(orbit_env.observations["y"]) < 1e-8

    orbit_env._set_var("x1",0)

    assert abs(orbit_env.observations["y"]) < 1e-8

test_orbit_environment()
print("Test successful")