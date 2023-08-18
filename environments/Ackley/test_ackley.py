from environments.Ackley import Environment
import numpy as np

def test_ackley_environment():
    ackley_env = Environment(None, {})

    variables = ackley_env.variables

    for key in variables.keys():
        assert variables[key] == 0 

    ackley_env._set_var("x1",1)

    assert abs(ackley_env.observations["y"] - 1.225741171669696) < 1e-8

    ackley_env._set_var("x1",0)

    assert abs(ackley_env.observations["y"] - 0) < 1e-8

test_ackley_environment()
print("Test successful")