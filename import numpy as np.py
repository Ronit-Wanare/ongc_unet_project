import numpy as np
import platypus

# Set the problem parameters
n = 39
sigma_max = 20000000
delta_max = 0.04
aL = 0.5
aU = 2
b_bounds = range(1, 41)
h_bounds = range(1, 41)


# Define the problem
class CrossSection(platypus.Problem):
    def __init__(self, n, sigma_max, delta_max, aL, aU, *args, **kwargs):
        super().__init__(n*2, 2, 2 + n) 
        self.n = n
        self.sigma_max = sigma_max
        self.delta_max = delta_max
        self.aL = aL
        self.aU = aU
    
    def evaluate(self, solution):
        b = solution.variables[:self.n]
        h = solution.variables[self.n:]
        V = np.sum(np.array(b) * np.array(h))
        delta = np.max(np.array(h)/(12*1e9*0.3*(np.array(b)**3)/12))
        sigma = np.max(6*V*np.array(h)/(np.array(b)**2))/1e6

        # Initialize solution.constraints with default values
        solution.constraints = [0.0] * len(solution.constraints)

        # Constraints
        constraints = []

        # Sigma constraint
        constraints.append(sigma_max - sigma)

        # Delta constraint
        constraints.append(delta_max - delta)

        # Aspect ratio constraint
        for i in range(self.n):
            aspect_ratio = h[i] / b[i]
            if aspect_ratio < self.aL or aspect_ratio > self.aU:
                constraints.append(aspect_ratio - self.aU)
            else:
                constraints.append(0.0)

        # Return the evaluated objectives and constraints
        return [sigma, delta], constraints
        
problem = CrossSection(n, sigma_max, delta_max, aL, aU)

# Define the algorithm
algorithm = platypus.NSGAII(problem, pop_size=40, max_generations=500)

# Define the optimization problem
problem.types[:] = [platypus.Real(b_bounds[0], b_bounds[1]) for _ in range(n)] + \
                   [platypus.Real(h_bounds[0], h_bounds[1]) for _ in range(n)]

# Run the optimization
algorithm.run(500)
