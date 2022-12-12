from SALib.sample import saltelli
from SALib.analyze import sobol

# Define the model inputs
problem = {
  'num_vars': 2,
  'names': ['x1', 'x2'],
  'bounds': [[-1, 1], [-1, 1]]
}

# Generate samples
param_values = saltelli.sample(problem, 1000)

# Run model (example)
Y = x1 * x2

# Perform analysis
Si = sobol.analyze(problem, Y)

# Print the first-order sensitivity indices
print(Si['S1'])
