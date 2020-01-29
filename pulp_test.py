from pulp import *
import pandas as pd

# Define the problem
prob = LpProblem("Diet Optimization", LpMaximize)

# Define the data set to be used
df = pd.read_excel("nutrition_info.xlsx", nrows=11)

# Create a list of all the food items in the excel sheet
food_items = list(df['Food Items'])

# Create dictionaries for each of the nutrition categories by name
# Could probably have been simplified with a for loop and iterating over
# food_items, but then we wouldn't have nicely named variables.
calories = dict(zip(food_items, df['Calories']))
calories_from_fat = dict(zip(food_items, df['Calories from Fat']))
fat = dict(zip(food_items, df['Fat (g)']))
saturated_fat = dict(zip(food_items, df['Saturated Fat (g)']))
trans_fat = dict(zip(food_items, df['Trans Fat (g)']))
cholesterol = dict(zip(food_items, df['Cholesterol (mg)']))
sodium = dict(zip(food_items, df['Sodium (mg)']))
carbs = dict(zip(food_items, df['Carbs (g)']))
dietary_fiber = dict(zip(food_items, df['Dietary Fiber (g)']))
sugar = dict(zip(food_items, df['Sugar (g)']))
protein = dict(zip(food_items, df['Protein (g)']))

# Define the scope of the optimization solution, i.e. the variables will be nonnegative
# in this case.
food_vars = LpVariable.dicts("Food", food_items, lowBound=0, cat='Continuous')

# The objective function: dietary_fiber was selected for maximization.
prob += lpSum([dietary_fiber[i]*food_vars[i] for i in food_items])

prob += lpSum([calories[f] * food_vars[f] for f in food_items]) >= 0, "CalorieMinimum"
#prob += lpSum([calories[f] * food_vars[f] for f in food_items]) <= 4000, "CalorieMaximum"
prob += lpSum([calories_from_fat[f] * food_vars[f] for f in food_items]) >= 0, "CaloriesFromFatMinimum"
#prob += lpSum([calories_from_fat[f] * food_vars[f] for f in food_items]) <= 1500, "CaloriesFromFatMaximum"
prob += lpSum([fat[f] * food_vars[f] for f in food_items]) >= 0, "FatMinimum"
#prob += lpSum([fat[f] * food_vars[f] for f in food_items]) <= 110, "FatMaximum"
#prob += lpSum([saturated_fat[f] * food_vars[f] for f in food_items]) >= 0, "SaturatedFatMinimum"
prob += lpSum([saturated_fat[f] * food_vars[f] for f in food_items]) <= 400, "SaturatedFatMaximum"
#prob += lpSum([trans_fat[f] * food_vars[f] for f in food_items]) >= 0, "TransFatMinimum"
prob += lpSum([trans_fat[f] * food_vars[f] for f in food_items]) <= 200, "TransFatMaximum"
#prob += lpSum([cholesterol[f] * food_vars[f] for f in food_items]) >= 0, "CholesterolMinimum"
prob += lpSum([cholesterol[f] * food_vars[f] for f in food_items]) <= 1000, "CholesterolMaximum"
#prob += lpSum([sodium[f] * food_vars[f] for f in food_items]) >= 0, "SodiumMinimum"
prob += lpSum([sodium[f] * food_vars[f] for f in food_items]) <= 10000, "SodiumMaximum"
prob += lpSum([carbs[f] * food_vars[f] for f in food_items]) >= 0, "CarbsMinimum"
#prob += lpSum([carbs[f] * food_vars[f] for f in food_items]) <= 300, "CarbsMaximum"
#prob += lpSum([sugar[f] * food_vars[f] for f in food_items]) >= 0, "SugarMinimum"
prob += lpSum([sugar[f] * food_vars[f] for f in food_items]) <= 500, "SugarMaximum"
prob += lpSum([protein[f] * food_vars[f] for f in food_items]) >= 0, "ProteinMinimum"
#prob += lpSum([protein[f] * food_vars[f] for f in food_items]) <= 120, "ProteinMaximum"
print(prob)

prob.solve()

print(f"Status: {LpStatus[prob.status]}")



