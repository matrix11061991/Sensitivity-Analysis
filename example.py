from SALib import ProblemSpec
from SALib.test_functions import Ishigami

import numpy as np

# By convention, we assign to "sp" (for "SALib Problem")
sp = ProblemSpec({
  'names': ['x1', 'x2', 'x3'],   # Name of each parameter
  'bounds': [[-np.pi, np.pi]]*3,  # bounds of each parameter
  'outputs': ['Y']               # name of outputs in expected order
})

(sp.sample_saltelli(1024, calc_second_order=True)
   .evaluate(Ishigami.evaluate)
   .analyze_sobol(print_to_console=True))

print(sp)

# Samples, model results and analyses can be extracted:
print(sp.samples)
print(sp.results)
print(sp.analysis)

# Basic plotting functionality is also provided
sp.plot()
