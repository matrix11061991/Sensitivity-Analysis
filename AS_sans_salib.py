# Define the model inputs
inputs = [
  {'name': 'x1', 'bounds': [-1, 1]},
  {'name': 'x2', 'bounds': [-1, 1]}
]

# Define the number of samples to use in the analysis
num_samples = 1000

# Generate samples
samples = []
for input in inputs:
  samples.append(np.linspace(input['bounds'][0], input['bounds'][1], num_samples))

# Run the model for each combination of input values
results = []
for x1, x2 in zip(*samples):
  result = x1 * x2
  results.append(result)

# Calculate the sensitivity indices
S1 = []
S2 = []
for i in range(len(inputs)):
  S1.append(np.var(results, axis=i) / np.var(results))
  S2.append(np.cov(samples[i], results)[0, 1] / np.var(results))

# Print the first-order sensitivity indices
print(S1)
