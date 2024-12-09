The propagation module have the tast to propagate a spacecraft using GMAT,
and with python algorithms avoid possible collisions with space debris

The module have an order of the files:
0. "load_gmat.py" The GMAT API startup file
1. "Spacecraft.py" The creation of the spacecraft using GMAT, including all the modeling of forces and propagation
2. "Functions.py" The file has some functions, those functions will be useful during the operation
3. "Simulation.py" The performing of the propagation simulation, and the storage of navigation data
4. "Plotting.py" The plotting of the obtained navigation data, alongside with the used debris data

The user can perform only the simulations by running only the "Simulation.py" file
or run the simulations and do their respective plotting by runnung only the "Plotting.py" file