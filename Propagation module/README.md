The propagation module have the tast to propagate a spacecraft using GMAT,
and with python use algorithms to avoid possible collisions with space debris

The module have an order of the files:
0. "load_gmat.py" The GMAT API startup file
1. "Spacecraft.py" The creation of the spacecraft using GMAT, including all the modeling of forces and propagation, here the user can edit the parameters of the spacefract according to the needs
2. "Functions.py" The file has some functions, those functions will be useful during the operation
3. "Simulation.py" The performing of the propagation simulation, and the storage of navigation data, here the user can choose the steps between each iteration, and the execution time of the simulation
4. "Plotting.py" The plotting of the obtained navigation data, alongside with the used debris data

The user can perform only the simulations by running only the "Simulation.py" file
or run the simulations and do their respective plotting by runnung only the "Plotting.py" file

Important: If the user perform changes in a file, the code in the same file needs to be runned to se its further effects