import pulp

model = pulp.LpProblem('Max produced', pulp.LpMaximize)

lemonada = pulp.LpVariable('limonada', lowBound = 0, cat = 'integer')
juice = pulp.LpVariable('juice', lowBound = 0, cat = 'integer')

model += 2 * lemonada + 1 * juice <= 100, 'water'
model += 1 * lemonada <= 50, 'sugar'
model += 1 * lemonada <= 30, 'limon_juice'
model += 2 * juice <= 40, 'fruits'

max_produce = lemonada + juice
model += max_produce, 'max_produce'

model.solve()

print(f"Company needs to produce {lemonada.varValue} of lemonada and {juice.varValue} of juice to use maximum of products icluding existing limits")

