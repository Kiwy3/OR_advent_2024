from ortools.linear_solver import pywraplp
import numpy as np

# init before loading
file_path = "instance.txt"
n = 0
j,i,k = (0,0,0)


# load instance
with open(file_path, 'r') as file:
    for line in file:
        if line.startswith('#') or line.startswith('\n'):continue
        if n==0 : 
            n,m = line.split()
            n=int(n)
            m=int(m)
            global_costs = np.zeros((n,m), dtype=float)
            Capa = np.zeros(n, dtype=int)
            Fixed = np.zeros(n, dtype=float)
            demand = np.zeros(m, dtype=int)
            continue
        if k<n : 
            Capa[k],Fixed[k] = line.split()
            k+=1
            continue
        if len(line.split())>1 :
            for num in line.split():
                try : global_costs[i][j] = num
                except : pass # print("error : ",i,j)
                i +=1
        else :
            demand[j] = line
            j+=1
            i=0

demand = demand.tolist()

# Add new variables
costs = np.divide(global_costs,demand) #unit cost
M = sum(demand[j] for j in range(m))

# Create Solver
solver = pywraplp.Solver.CreateSolver('SCIP')
if not solver:
    raise Exception("Solver not created.")

# Define variables
x = {}
y = {}
for i in range(n):
    y[i] = solver.BoolVar(f'y[{i}]')
    for j in range(m):
        x[i, j] = solver.IntVar(lb=0, ub=100000, name=f'x[{i,j}]')

# Objective
objective = []
for i in range(n):
    objective.append(y[i]*Fixed[i])
    for j in range(m):   
        objective.append(costs[i][j] * x[i, j])
solver.Minimize(solver.Sum(objective))

# Constraints

# (1) Each client demand is handled
for j in range(m):
    solver.Add(solver.Sum(x[i, j] for i in range(n)) == demand[j])

# (2) respect max capacity of each warehouse
for i in range(n):
    solver.Add(solver.Sum(x[i, j] for j in range(m)) <= Capa[i])

# (3) Each client is assigned to at most one warehouse
for i in range(n):
    solver.Add(solver.Sum(x[i, j] for j in range(m)) <= y[i]*M)

# Solve the problem
status = solver.Solve()

# Clear the file
with open("solution.txt", "w") as file:
    pass 

fixed_cost = 0
variable_cost = 0

# Check the results
if status == pywraplp.Solver.OPTIMAL:
    print("Solution found!")
    print(f"Total cost: {solver.Objective().Value()}")
    for i in range(n):
        fixed_cost+= Fixed[i]*y[i].solution_value()
        with open("solution.txt", "a") as file:
            file.write(f"warehouse {i} is {
            "open" if y[i].solution_value()==1 else "closed"
            } \n" )


        for j in range(m):
            variable_cost+= costs[i][j]*x[i, j].solution_value()
            if x[i, j].solution_value() > 0:
                with open("solution.txt", "a") as file:
                    file.write(f"\t {x[i, j].solution_value()} products of client {j} with Cost {costs[i, j]*x[i, j].solution_value()}\n")
else:
    print("No optimal solution found!")
print("Fixed cost : ",fixed_cost)
print("Variable cost : ",variable_cost)

# Export the results
import pandas as pd
export = np.zeros_like(costs)
for i in range(n):
    for j in range(m):
        export[i][j] = x[i, j].solution_value()

df = pd.DataFrame(export,
                  columns=[f"Warehouse_{j}" for j in range(m)],
                  index=[f"Client_{i}" for i in range(n)])
df.to_csv("export.csv")

import matplotlib.pyplot as plt
from matplotlib import colormaps


for i in range(n):
    for j in range(m):
        if export[i,j]>0:
            plt.barh(f"Warehouse_{i+1}",
                    export[i,j],
                    left = export[i,:j].sum(),
                    label = f"Client {j}",
                    color = colormaps["tab20b_r"](j/m)
                    )
            plt.text(export[i,:j].sum()+export[i,j]/2,f"Warehouse_{i+1}",f"c_{j}")
        else : 
            plt.barh(f"Warehouse_{i+1}",0)
    plt.title("warehouse allocation")
    plt.savefig("allocation.png")