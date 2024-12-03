import numpy as np
from ortools.linear_solver import pywraplp

# Read instance data
file_path = "instance.txt"
n, m, C = np.loadtxt(file_path, skiprows=13, max_rows=1, dtype=int)
connections = np.loadtxt(file_path, skiprows=14, dtype=int)

# Parse connection data
s, e, d, c = connections[:, 0], connections[:, 1], connections[:, 2], connections[:, 3]

# Create solver
solver = pywraplp.Solver.CreateSolver('SCIP')
if not solver:
    raise Exception("Solver not created.")

# Define decision variables
x = {}
for i in range(m):
    x[i] = solver.BoolVar(f'x[{i}]')

# Objective function: Minimize total cost
solver.Minimize(solver.Sum(d[i] * x[i] for i in range(m)))

# Budget constraint
solver.Add(solver.Sum(c[i] * x[i] for i in range(m)) <= C)

# Flow conservation constraints
#  Start node (city 1): 1 outgoing connection
solver.Add(solver.Sum(x[i] for i in range(m) if s[i] == 1) == 1)

#  End node (city 100): 1 incoming connection
solver.Add(solver.Sum(x[i] for i in range(m) if e[i] == 100) == 1)

#  Intermediate nodes: Flow conservation
for j in range(2, n):#2 to n-1
    incoming = solver.Sum(x[i] for i in range(m) if e[i] == j)
    outgoing = solver.Sum(x[i] for i in range(m) if s[i] == j)
    solver.Add(incoming == outgoing)

# Solve the problem
status = solver.Solve()

# Output results
if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
    print("Solution found!")
    print(f"Total distance: {solver.Objective().Value()}")
    path = []
    for i in range(m):
        if x[i].solution_value() > 0.5:
            path.append((s[i], e[i]))
else:
    print("No optimal solution found!")
    if status == pywraplp.Solver.INFEASIBLE:
        print("Problem is infeasible.")
    elif status == pywraplp.Solver.UNBOUNDED:
        print("Problem is unbounded.")
    else:
        print("Unknown solver status.")

t = 1
with open("solution.txt", "w") as file:
    file.write("Total distance: " + str(solver.Objective().Value())+"\n")
    file.write("Total cost: " +
               str(sum(c[i] * x[i].solution_value() for i in range(m)))
               +"\n")
    for j in range(len(path)):
        for i in range(len(path)):
            if t == path[i][0]:
                t = path[i][1]
                file.write(f"Connection {path[i][0]} -> {path[i][1]}, Distance: {d[path[i][0]]}, Cost: {c[path[i][0]]}\n")
                print(i)
    


            
