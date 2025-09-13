"""
CST-305: Project 1 – Visualize ODE with SciPy
Luke Hoyle, Kian Knudegaard
Prof. Ricardo Citro
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the ODE: dT/dt = -k*(T - Tamb) + P
def cpu_temp(T, t, k, Tamb, P):
    return -k * (T - Tamb) + P

# Get the user input and set the parameters
k = float(input("Enter cooling constant k: "))
Tamb = float(input("Enter ambient temperature (°C): "))
P = float(input("Enter power input: "))
T0 = float(input("Enter initial CPU temperature (°C): "))
t_max = float(input("Enter simulation time (seconds): "))

# Time points
t_vals = np.linspace(0, t_max, 300)

# Solve ODE
T_vals = odeint(cpu_temp, T0, t_vals, args=(k, Tamb, P))

# odeint returns a 2D array (n_points x n_vars), flatten it
T_vals = T_vals.flatten()

# Plot
plt.figure(figsize=(8,5))
plt.plot(t_vals, T_vals, label="CPU Temperature", linewidth=2)
plt.axhline(y=Tamb, color='gray', linestyle='--', label="Ambient Temp")

plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.title("CPU Temperature Simulation using ODEINT")
plt.legend()
plt.grid(True)
plt.show()
