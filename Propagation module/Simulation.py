import time as t
from Functions import *
from Spacecraft import *

# Simulation

# Read and load debris data from a csv file
debris_file_path = r"CSV's\Punctual debris.csv"
debris = read_debris(debris_file_path)

# Simulation parameters (Adjust depending on requirements)
step = 100.0  # Step between iteration (seconds)
safe_distance = 1000.0  # Minimun safe distance between the spacecraft and the debris (kilometers)

# Variables during the simulation
# Creating arrays with the positions of the spacecraft, these arrays will be updated for future ploting
time = 0.0 # Initial time
#Input the initial positon of the spacecraft
x_position = [6000]
y_position = [0]
z_position = [0]

# Starting the propagation simulation
print("Starting simulation...")
for x in range(60):  # Adjust number of steps, in this case will be 60
    #Perform a step
    IG.Step(step)
    time += step
    
    # Get the actual state vector of the spacecraft
    state = IG.GetState()  # [X, Y, Z, VX, VY, VZ]
    SC_pos = [state[0], state[1], state[2]]
    
    # Adding the actual SC_pos to the previous created arrays 
    x_position.append(SC_pos[0])
    y_position.append(SC_pos[1])
    z_position.append(SC_pos[2])
    
    # Analysing proximity with debris
    for debris_pos in debris:
        distance = calculate_distance(SC_pos, debris_pos)
        if distance < safe_distance:
            # Alert
            t.sleep(1)
            print_in_color(f"¡Collision hazard detected! Detected debris at: {distance} km. Executing avoidance maneuver...", 31) # 31 its the code for color red in the function 
            t.sleep(1)
            
            # Configuration of the delta-V
            # Lets see if the debris is in a lower or a higher orbit
            SC_pos_magnitude = np.linalg.norm(SC_pos)
            debris_pos_magnitude = np.linalg.norm(debris_pos)
            if debris_pos_magnitude < SC_pos_magnitude:
                delta_v = [+0.5, +0.5, 0]  # Go to a higher orbit (km/s)
            else:
                delta_v = [-0.5, -0.5, 0]  # Go to a lower orbit (km/s)
            
            # Delta-V maneuver
            
            # Applying delta-V
            state[3] += delta_v[0]  # Adjusting VX
            state[4] += delta_v[1]  # Adjusting VY
            state[5] += delta_v[2]  # Adjusting VZ
            print_in_color(f"¡Maneuver applied successfuly! Time: {time} s, State: {IG.GetState()}", 32) # 2 is the code for green color
            
            # Updating the state vector of the spacecraft
            SC.SetField("X", state[0])
            SC.SetField("Y", state[1])
            SC.SetField("Z", state[2])
            SC.SetField("VX", state[3])
            SC.SetField("VY", state[4])
            SC.SetField("VZ", state[5])
            
            # Updating the propagator state
            gmat.Initialize()
            PROP.PrepareInternals()
            
            # Lets apply another delta-V after a while to get to an orbit similar to the previous one
            # Propagate the spacecraft a while
            for x in range(50):  # Ajust the number of steps taken, here we do 100
                #Perform a step
                IG.Step(step)
                time += step
                
                # Obtaining the actual state vector
                state = IG.GetState()  # [X, Y, Z, VX, VY, VZ]
                SC_pos = [state[0], state[1], state[2]]
                
                # Not forget to update the arrays with the positions
                x_position.append(state[0])
                y_position.append(state[1])
                z_position.append(state[2])
                
                # Printing actual state of the spacecraft
                print(f"Time: {time} s, State vector: {IG.GetState()}")
            
            # Delta-V maneuver
            # Note that the values are multiplied by 0.8, this is because we dont want to get back at the same orbit with the risk of collision
            state[3] -= 0.8 * delta_v[0]  # Adjusting VX
            state[4] -= 0.8 * delta_v[1]  # Adjusting VY
            state[5] -= 0.8 * delta_v[2]  # Adjusting VZ
            print_in_color(f"¡Maneuver applied successfuly! Time: {time} s, State: {IG.GetState()}", 32) # 2 is the code for green color
            
            # Updating the state vector of the spacecraft
            SC.SetField("X", state[0])
            SC.SetField("Y", state[1])
            SC.SetField("Z", state[2])
            SC.SetField("VX", state[3])
            SC.SetField("VY", state[4])
            SC.SetField("VZ", state[5])
            
            # Updating the propagator state
            gmat.Initialize()
            PROP.PrepareInternals()
            
            break  # Break after the delta-V maneuver
    
    # Printing actual state of the spacecraft
    print(f"Time: {time} s, State vector: {IG.GetState()}")

print("The simulation was done.")
