from ortools.linear_solver import pywraplp

def solve_railway_cover(num_segments, num_contracts, included, cost):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        raise Exception("Solver not created. Ensure OR-Tools is installed correctly.")

    # Variables: pick[c] is 1 if contract c is chosen, otherwise 0
    pick = {}
    for c in range(num_contracts):
        pick[c] = solver.BoolVar(f'pick[{c}]')



    # Objective: Minimize total cost
    objective = solver.Objective()
    for c in range(num_contracts):
        objective.SetCoefficient(pick[c], cost[c])
    objective.SetMinimization()

    # Constraints: Each segment must be covered by at least one contract
    for s in range(num_segments):
        constraint = solver.Constraint(1, solver.infinity(), f'Cover[{s}]')
        for c in range(num_contracts):
            if s in included[c]:
                constraint.SetCoefficient(pick[c], 1)

                
    solver.SetTimeLimit(60000)  # Time limit in milliseconds (e.g., 60 seconds)

    # Solve the problem
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Optimal solution found.')
        print('Total Cost =', solver.Objective().Value())
        selected_contracts = [c for c in range(num_contracts) if pick[c].solution_value() > 0.5]
        print('Selected Contracts:', selected_contracts)
        return selected_contracts, solver.Objective().Value()
    else:
        print('No optimal solution found.')
        return None, None

def load_instance(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Read the first line for number of segments and contracts
    num_segments, num_contracts = map(int, lines[0].strip().split())

    # Initialize cost and included
    cost = []
    included = {}

    # Read the rest of the lines for cost and segment sets
    for idx, line in enumerate(lines[1:]):
        parts = list(map(int, line.strip().split()))
        cost.append(parts[0])
        included[idx] = parts[1:]

    return num_segments, num_contracts, included, cost

# Example usage with instance file
instance_file = 'instance_clean.txt'
num_segments, num_contracts, included, cost = load_instance(instance_file)
solve_railway_cover(num_segments, num_contracts, included, cost)