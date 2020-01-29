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
item_count = dict(zip(food_items, df['Item Count']))

# Define the scope of the optimization solution, i.e. the variables will be nonnegative
# in this case.
food_vars = LpVariable.dicts("Food", food_items, lowBound=0, cat=LpInteger)

# The objective function: dietary_fiber was selected for maximization.
prob += lpSum([dietary_fiber[i]*food_vars[i] for i in food_items])

# Calories
prob += lpSum([calories[f] * food_vars[f] for f in food_items]) >= 2000, "CalorieMinimum"

# Calories from fat
prob += lpSum([calories_from_fat[f] * food_vars[f] for f in food_items]) >= 585, "CaloriesFromFatMinimum"

# Fat
prob += lpSum([fat[f] * food_vars[f] for f in food_items]) >= 64.5, "FatMinimum"

# Saturated fat
prob += lpSum([saturated_fat[f] * food_vars[f] for f in food_items]) <= 27, "SaturatedFatMaximum"

# Trans fat
prob += lpSum([trans_fat[f] * food_vars[f] for f in food_items]) <= 27, "TransFatMaximum"

# Cholesterol
prob += lpSum([cholesterol[f] * food_vars[f] for f in food_items]) <= 250, "CholesterolMaximum"

# Sodium
prob += lpSum([sodium[f] * food_vars[f] for f in food_items]) >= 1000, "SodiumMinimum"

# Carbs
prob += lpSum([carbs[f] * food_vars[f] for f in food_items]) >= 130, "CarbsMinimum"

# Sugar
prob += lpSum([sugar[f] * food_vars[f] for f in food_items]) <= 50, "SugarMaximum"

# Protein
prob += lpSum([protein[f] * food_vars[f] for f in food_items]) >= 56, "ProteinMinimum"

# Item Count
prob += lpSum([item_count[f] * food_vars[f] for f in food_items]) == 4, "ItemCountEquals"

prob.solve()

print(f"Status: {LpStatus[prob.status]}")

total_val = 0

for v in prob.variables():
    if v.varValue > 0:
        print(f"{v.name} = {v.varValue}")
        total_val += (v.varValue * dietary_fiber[v.name.replace('_', ' ')[5:]])
    elif v.varValue < 0:
        print("Error: value less than 0. Cannot have negative food quantities.")

if LpStatus[prob.status] == "Optimal":
    print(f"Maximized dietary fiber amount: {total_val} (g)")

