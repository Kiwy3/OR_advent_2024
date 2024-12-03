from gurobipy import Model, GRB, quicksum
import numpy as np

# Parameters
n = 100  # number of cities
C = 73   # max cost
# Example data for distances and costs (replace these with your actual data)
file_path = "day_2/instance.txt"


# Read data
n, m, C = np.loadtxt(file_path, skiprows=13,max_rows=1, usecols=[0,1,2])
connections = np.loadtxt(file_path, skiprows=14, usecols=[0,1,2,3])

# Initialize Gurobi model
model = Model("Network Design")

# Decision variables: x[i] is 1 if connection i is selected, 0 otherwise
x = model.addVars(len(connections), vtype=GRB.BINARY, name="x")

# Objective: Minimize total distance
model.setObjective(
    quicksum(connections[i][2] * x[i] for i in range(len(connections))),
    GRB.MINIMIZE
)

# Constraint 1: Total cost must not exceed max_budget
model.addConstr(
    quicksum(connections[i][3] * x[i] for i in range(len(connections))) <= C,
    "BudgetConstraint"
)

# Constraint 2: Connectivity constraint (use Kruskal's MST approach)
# Subtour elimination constraints (Miller-Tucker-Zemlin formulation for TSP-like problems)
# Use an auxiliary variable for connectivity
u = model.addVars(n, vtype=GRB.CONTINUOUS, lb=0, name="u")

for i, (city1, city2, _, _) in enumerate(connections):
    model.addConstr(
        u[city1 - 1] - u[city2 - 1] + (n - 1) * x[i] <= n - 2
    )

# Solve the model
model.optimize()

# Print the results
if model.status == GRB.OPTIMAL:
    print("\nOptimal solution found!")
    print(f"Total Distance: {model.objVal}")
    print("Selected Connections:")
    for i in range(len(connections)):
        if x[i].x > 0.5:  # Variable is binary, so check if it's selected
            print(f"Connection {connections[i]} selected.")
else:
    print("No optimal solution found.")