from ortools.sat.python import cp_model

def load_data(filename):
    events = []
    n=0
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('#') or line.startswith('\n'):
                continue
            if n>0 :
                start = int(line.split()[1])
                end = int(line.split()[2])
                events.append((start, end))
            else : n,m = line.split();n=int(n);m=int(m)

    return events



def solve_day01(events):
    # Create the model
    model = cp_model.CpModel()

    # Create the variables
    num_rooms = len(events)
    room_assignments = {}
    for i, event in enumerate(events):
        room_assignments[i] = model.NewIntVar(0, num_rooms - 1, f'room_{i}')

    # Add the constraints
    for i, event1 in enumerate(events):
        for j, event2 in enumerate(events):
            if i != j and event1[0] < event2[1] and event2[0] < event1[1]:
                model.Add(room_assignments[i] != room_assignments[j])

    # Add the objective function
    model.Minimize(model.NewIntVar(0, num_rooms - 1, 'num_rooms'))

    # Solve the problem
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    # Print the solution
    if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
        num_rooms_used = 0
        for i, event in enumerate(events):
            room = solver.Value(room_assignments[i])
            if room > num_rooms_used:
                num_rooms_used = room
        print('Number of rooms used:', num_rooms_used + 1)
    else:
        print('No solution found')


filename = 'instance.txt'
events = load_data(filename)
solve_day01(events)