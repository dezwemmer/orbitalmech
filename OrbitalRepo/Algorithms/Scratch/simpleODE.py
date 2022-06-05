# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Orbital Mechanics & Dynamics Software Collection
# Author:   Steven Anderson
# Created:  JUN 2022
# Brief:    Simple ODE solution usuing odeint
# 
#           
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# Model
def model(state, t):
    k = 0.3
    x = state[0]
    x_dot = -k * x
    dstate_dt = [x_dot]
    return dstate_dt

# Initial Conditions (easy to add more vars)
x0 = 2
state = [x0]

# Time Array
t = np.linspace(0, 20)

# Solving ODE
sol = odeint(model, state, t)
x_sol = sol[:,0]

# Plotting
plt.plot(t,x_sol)
plt.xlabel("time")
plt.ylabel("x(t)")
plt.show()
