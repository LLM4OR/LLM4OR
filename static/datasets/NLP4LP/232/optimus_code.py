# Code automatically generated from OptiMUS

# Problem type: MIP        
# Problem description
'''
A restaurant offers two types of meals: Original and Experimental. The Original
meal generates OriginalFoodWaste units of food waste and OriginalWrappingWaste
units of wrapping waste, and requires OriginalCookingTime minutes to prepare.
The Experimental meal generates ExperimentalFoodWaste units of food waste and
ExperimentalWrappingWaste units of wrapping waste, and requires
ExperimentalCookingTime minutes to prepare. The total wrapping waste must not
exceed MaxWrappingWaste, and the total food waste must not exceed MaxFoodWaste.
Determine the number of Original and Experimental meals to minimize the total
cooking time.
'''
# Import necessary libraries
import json
from gurobipy import *
     
# Create a new model
model = Model()

# Load data 
with open("/Users/gaowenzhi/Desktop/optimus-OR-paper/data/new_dataset/sample_datasets/233/parameters.json", "r") as f:
    data = json.load(f)
    
# @Def: definition of a target
# @Shape: shape of a target
        
# Parameters 
# @Parameter OriginalFoodWaste @Def: Food waste generated by the original meal @Shape: [] 
OriginalFoodWaste = data['OriginalFoodWaste']
# @Parameter OriginalWrappingWaste @Def: Wrapping waste generated by the original meal @Shape: [] 
OriginalWrappingWaste = data['OriginalWrappingWaste']
# @Parameter OriginalCookingTime @Def: Cooking time for the original meal @Shape: [] 
OriginalCookingTime = data['OriginalCookingTime']
# @Parameter ExperimentalFoodWaste @Def: Food waste generated by the experimental meal @Shape: [] 
ExperimentalFoodWaste = data['ExperimentalFoodWaste']
# @Parameter ExperimentalWrappingWaste @Def: Wrapping waste generated by the experimental meal @Shape: [] 
ExperimentalWrappingWaste = data['ExperimentalWrappingWaste']
# @Parameter ExperimentalCookingTime @Def: Cooking time for the experimental meal @Shape: [] 
ExperimentalCookingTime = data['ExperimentalCookingTime']
# @Parameter MaxWrappingWaste @Def: Maximum allowed wrapping waste @Shape: [] 
MaxWrappingWaste = data['MaxWrappingWaste']
# @Parameter MaxFoodWaste @Def: Maximum allowed food waste @Shape: [] 
MaxFoodWaste = data['MaxFoodWaste']

# Variables 
# @Variable OriginalMeals @Def: The number of Original meals @Shape: [] 
OriginalMeals = model.addVar(vtype=GRB.INTEGER, name="OriginalMeals")
# @Variable ExperimentalMeals @Def: The number of Experimental meals @Shape: [] 
ExperimentalMeals = model.addVar(vtype=GRB.INTEGER, name="ExperimentalMeals")

# Constraints 
# @Constraint Constr_1 @Def: The total wrapping waste generated by Original and Experimental meals must not exceed MaxWrappingWaste.
model.addConstr(OriginalWrappingWaste * OriginalMeals + ExperimentalWrappingWaste * ExperimentalMeals <= MaxWrappingWaste)
# @Constraint Constr_2 @Def: The total food waste generated by Original and Experimental meals must not exceed MaxFoodWaste.
model.addConstr(OriginalMeals * OriginalFoodWaste + ExperimentalMeals * ExperimentalFoodWaste <= MaxFoodWaste)

# Objective 
# @Objective Objective @Def: The total cooking time is the sum of the cooking times required for Original and Experimental meals. The objective is to minimize the total cooking time.
model.setObjective(OriginalCookingTime * OriginalMeals + ExperimentalCookingTime * ExperimentalMeals, GRB.MINIMIZE)

# Solve 
model.optimize()

# Extract solution 
solution = {}
variables = {}
objective = []
variables['OriginalMeals'] = OriginalMeals.x
variables['ExperimentalMeals'] = ExperimentalMeals.x
solution['variables'] = variables
solution['objective'] = model.objVal
with open('solution.json', 'w') as f:
    json.dump(solution, f, indent=4)
