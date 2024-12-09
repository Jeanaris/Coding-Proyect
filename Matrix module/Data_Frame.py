import pandas as pd

#Creating Data Frame with the features of the orbits 
data = {
    "Type of Orbit": ["LEO", "MEO", "GEO", "HEO"],
    "Height (km)": [500, 20000, 35786, 40000],
    "Eccentricity": [0, 0.1, 0, 0.7],
    "Inclination (°)": [90, 55, 0, 30],
    "Orbital Period (min)": [90, 720, 1440, 2880],
    "Orbital Speed (km/s)": [7.8, 3.9, 3.1, 2.8],
    "Space Radiation (Sv/year)": [0.25, 1.2, 2.5, 5.0],
    "Earth Coverage (%)": [30, 60, 100, 80],
    "Coverage Persistance (min/hour)": [10, 30, 60, 45],
    "Signal Latency (ms)": [5, 40, 120, 200],
    "Launch Cost (USD/kg)": [5000, 15000, 25000, 40000],
    "Fuel Needed (kg)": [500, 800, 1200, 2000],
    "Collision Risk": ["High", "Medium", "Low", "Low"]
}

#Creating Data Frame with pandas 
df = pd.DataFrame(data)

#Show Data Frame
print("Orbit options available:")
print(df)

