# import libraries
from ortools.linear_solver import pywraplp
import numpy as np

# init before loading
file_path = "instance.txt"
n = 0
data = []

# load instance
with open(file_path, 'r') as file:
    for line in file:
        if line.startswith('#') or line.startswith('\n'):continue
        if n>0 :
            for i in line.split():
                data.append(int(i))
        else : n = int(line)
m = n # number of tasks
costs = np.array(data, dtype=float).reshape((n,n))


# Create Solver
solver = pywraplp.Solver.CreateSolver('SCIP')
if not solver:
    raise Exception("Solver not created.")

# Define variable (x_ij)
x = {}
for i in range(n):
    for j in range(m):
        x[i, j] = solver.BoolVar(f'x[{i},{j}]')

# Objective function
objective = []
for i in range(n):
    for j in range(m):   
        objective.append(costs[i][j] * x[i, j])
solver.Minimize(solver.Sum(objective))

# Constraints
# (1) Each task is assigned to exactly one employee
for j in range(m):
    solver.Add(solver.Sum(x[i, j] for i in range(n)) == 1)

# (2) Each employee is assigned to exactly one task
for i in range(n):
    solver.Add(solver.Sum(x[i, j] for j in range(n)) == 1)

# Solve the problem
status = solver.Solve()

# Clear the file
with open("solution.txt", "w") as file:
    pass 

# Check the results
if status == pywraplp.Solver.OPTIMAL:
    print("Solution found!")
    print(f"Total cost: {solver.Objective().Value()}")
    assignment = []
    for i in range(n):
        for j in range(m):
            if x[i, j].solution_value() > 0.5:  # Boolean variable, so close to 1 means selected
                assignment.append((i, j))
                with open("solution.txt", "a") as file:
                    file.write(f"Employee {i} assigned to Task {j} with Cost {costs[i, j]}\n")
else:
    print("No optimal solution found!")




