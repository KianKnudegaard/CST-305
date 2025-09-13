# CPU Temperature Simulation (CST-305 Project 1)

## Description
This project models CPU heat dissipation using an ordinary differential equation (ODE). 
The goal is to show how CPU temperature changes over time, depending on ambient temperature, 
cooling constant, and power input. This helps engineers evaluate cooling system effectiveness.

## Requirements
To run this program, you need:
- Python 3.x
- numpy
- scipy
- matplotlib

Install dependencies with:
```bash
pip install numpy scipy matplotlib
```

## How to Run
1. Run the Python script in your terminal or IDE.
2. Enter the required input values when prompted:
   - Cooling constant (k)
   - Ambient temperature (°C)
   - Power input
   - Initial CPU temperature (°C)
   - Simulation time (seconds)
3. The program will solve the ODE and display a plot of CPU temperature over time.

## Example
```bash
python cpu_temp_simulation.py
```
You will see a graph showing CPU temperature vs. time.

## Authors
- Luke Hoyle
- Kian Knudegaard
