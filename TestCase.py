from ortools.sat.python import cp_model
import time

model = cp_model.CpModel()

# Input handling
line1 = input().split()
n, k = [int(i) for i in line1]
c = []
for i in range(2 * n + 1):
    str_ci = input().split()
    c_i = [int(j) for j in str_ci]
    c.append(c_i)

# Variable initialization
x = []
for i in range(2 * n + 1):
    x_i = []
    for j in range(2 * n + 1):
        if i == j:
            x_i.append(0)
        else:
            x_i.append(model.NewIntVar(0, 1, f'x[{i}][{j}]'))
    x.append(x_i)

y = [model.NewIntVar(1, 2 * n + 1, f'y[{i}]') for i in range(2 * n + 1)]
p = [model.NewIntVar(0, k, f'p[{i}]') for i in range(2 * n + 1)]

###### Constrains ----------------------------------------------------------
# One way in, one way out
for i in range(2 * n + 1):
    model.Add(sum(x[i][j] for j in range(2 * n + 1)) == 1)
    model.Add(sum(x[j][i] for j in range(2 * n + 1)) == 1)

# Start at city 0
model.Add(y[0] == 1)

# Number of passengers at city 0 equals 0
model.Add(p[0] == 0)

# No subcycles
for i in range(2 * n + 1):
    for j in range(1, 2 * n + 1):
        if i == j:
            continue
        model.Add(y[i] + 1 == y[j]).OnlyEnforceIf(x[i][j])

# Picks before drops
for i in range(n + 1, 2 * n + 1):
    model.Add(y[i] > y[i - n])

# Maximum k passengers
for i in range(2 * n + 1):
    for j in range(1, 2 * n + 1):
        if i == j:
            continue
        # Picks
        if j <= n:
            model.Add(p[j] - p[i] == 1).OnlyEnforceIf(x[i][j])
        # Drops
        if j > n:
            model.Add(p[i] - p[j] == 1).OnlyEnforceIf(x[i][j])

###### Objective -------------------------------------------------------
model.Minimize(sum(sum(x[i][j] * c[i][j] for j in range(2 * n + 1)) for i in range(2 * n + 1)))

###### Solve -----------------------------------------------------------
solver = cp_model.CpSolver()

stt = solver.Solve(model)
if stt == cp_model.OPTIMAL:
    sol = {}
    for i in range(2 * n + 1):
        sol[solver.Value(y[i])] = i
    sol = [sol[i + 1] for i in range(2 * n + 1)]
    print(n)
    for soll in sol:
        if soll != 0:
            print(soll, end=' ')
