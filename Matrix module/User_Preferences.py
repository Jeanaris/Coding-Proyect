#Creating a dictionary to store user preferences, taking account the score and value desired
user_preferences = {
    "Height (km)": {"score": 0, "desired_value": 0},
    "Eccentricity": {"score": 0, "desired_value": 0},
    "Inclination (°)": {"score": 0, "desired_value": 0},
    "Orbital Period (min)": {"score": 0, "desired_value": 0},
    "Orbital Speed (km/s)": {"score": 0, "desired_value": 0},
    "Space Radiation (Sv/year)": {"score": 0, "desired_value": 0},
    "Earth Coverage (%)": {"score": 0, "desired_value": 0},
    "Coverage Persistance (min/hour)": {"score": 0, "desired_value": 0},
    "Signal Latency (ms)": {"score": 0, "desired_value": 0},
    "Launch Cost (USD/kg)": {"score": 0, "desired_value": 0},
    "Fuel Needed (kg)": {"score": 0, "desired_value": 0}
}

#User assignment of points, the relative importance designated by "score" and the desired value of the object
user_preferences["Height (km)"] = {"score": float(input(f'Importance level of Height: ')), "desired_value": float(input(f'Desired value of Height (km): '))}
user_preferences["Eccentricity"] = {"score": float(input(f'Importance level of Eccentricity: ')), "desired_value": float(input(f'Desired value of Eccentricity: '))}
user_preferences["Inclination (°)"] = {"score": float(input(f'Importance level of Inclination: ')), "desired_value": float(input(f'Desired value of Inclination (°): '))}
user_preferences["Orbital Period (min)"] = {"score": float(input(f'Importance level of Orbital Periord: ')), "desired_value": float(input(f'Desired value of Orbital Period (min): '))}
user_preferences["Orbital Speed (km/s)"] = {"score": float(input(f'Importance level of Orbital Speed: ')), "desired_value": float(input(f'Desired value of Orbital Speed (km/s): '))}
user_preferences["Space Radiation (Sv/year)"] = {"score": float(input(f'Importance level of Space Radiation: ')), "desired_value": float(input(f'Desired value of Space Radiation (Sv/year): '))}
user_preferences["Earth Coverage (%)"] = {"score": float(input(f'Importance level of Earth Coverage: ')), "desired_value": float(input(f'Desired value of Earth Coverage (%): '))}
user_preferences["Coverage Persistance (min/hour)"] = {"score": float(input(f'Importance level of Coverage Persistance: ')), "desired_value": float(input(f'Desired value of Coverage Persistance (min/hour): '))}
user_preferences["Signal Latency (ms)"] = {"score": float(input(f'Importance level of Signal Latency: ')), "desired_value": float(input(f'Desired value of Signal Latency (ms): '))}
user_preferences["Launch Cost (USD/kg)"] = {"score": float(input(f'Importance level of Launch Cost: ')), "desired_value": float(input(f'Desired value of Launch Cost (USD/kg): '))}
user_preferences["Fuel Needed (kg)"] = {"score": float(input(f'Importance level of Fuel Needed: ')), "desired_value": float(input(f'Desired value of Fuel Needed (kg): '))}

#Showing user preferences 

print("\nUser preferences:")
for feature, values in user_preferences.items():
    print(f"{feature}: Score={values['score']}, Desired Value={values['desired_value']}")
