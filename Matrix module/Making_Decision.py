import pandas as pd
from User_Preferences import user_preferences
from Data_Frame import df

#Funtion to calculate the score of a orbit taking acount the preferences
def calculate_score(orbits_df, preferences): 
    scores = []
    for index, orbit in orbits_df.iterrows(): #Using iterrows() the data frame wiil be read row by row
        total_score = 0
        for feature, config in preferences.items():
            score = config["score"]
            desired_value = config["desired_value"]
            if score > 0 and desired_value > 0:  #To avoid unweighted characteristics
                real_value = orbit[feature]
                #Calculating individual score 
                difference = abs(real_value - desired_value) #Calculating the difference bewteen the data and the desired value
                individual_score = score * (1 - (difference / desired_value)) #Calculating the individual score 
                total_score += max(individual_score, 0)  #Making sure that the score won't be negative
        scores.append(total_score)
    return scores

#Calculate scores creating a new column with the scores
df["Score"] = calculate_score(df, user_preferences)

#Showing the data frame with the scores
print("\Orbits with scores calculated:")
print(df.sort_values(by="Score", ascending=False)) #Orbits are sorted in descending order based on the socre column

print("------------------------------------------------------------------------------------------------------------")
print("The above shows the calculation done, from which it can be conclude that:")

#Select the orbit with the highest score
better_orbit = df.loc[df["Score"].idxmax()] #Taking the onw with highest score
print("\nBest selected orbit is: (With its features)")
print(better_orbit)

