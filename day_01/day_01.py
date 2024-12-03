import numpy as np
from ortools.linear_solver import pywraplp

# Read instance data
file_path = "instance.txt"
e = []
s = []
n = 0
with open(file_path, 'r') as file:
    for line in file:
        if line.startswith('#') or line.startswith('\n'):continue
        if n>0 :
            s.append(int(line.split()[1]))
            e.append(int(line.split()[2]))
        else : n,m = line.split();n=int(n);m=int(m)
bigM = n*m


# Create solver
solver = pywraplp.Solver.CreateSolver('SCIP')
if not solver:
    raise Exception("Solver not created.")

# Define decision variables
x = {}
y = {}
for i in range(n):
    y[i] = solver.BoolVar(f'y[{i}]')
    for k in range(n):
        x[i,k] = solver.BoolVar(f'x[{i},{k}]')

# Objective function: Minimize total cost
solver.Minimize(solver.Sum(y[k] for k in range(n)))

# conflict constraints
for j in range(m):
    for k in range(n):
        event_1 = x[s[j]-1,k]
        event_2 = x[e[j]-1,k]
        solver.Add((event_1 + event_2)<=1)

# One room by event
for i in range(n):
    solver.Add(solver.Sum(x[i,k] for k in range(n)) == 1)

# define Y
for k in range(n):
    solver.Add(solver.Sum(x[i,k] for i in range(n)) <= y[k]*bigM)

# Solve the problem
status = solver.Solve()

# Output results
if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
    path = []
    print("number of room : ",solver.Objective().Value())
    for k in range(n):
        for i in range(n):
            if x[i,k].solution_value() > 0.5:
                print(f"Event {i+1} -> Room {k+1}")
else:
    print("No optimal solution found!")
    if status == pywraplp.Solver.INFEASIBLE:
        print("Problem is infeasible.")
    elif status == pywraplp.Solver.UNBOUNDED:
        print("Problem is unbounded.")
    else:
        print("Unknown solver status.")
    


            
