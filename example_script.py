from mcmc import MCMC

import numpy as np
import matplotlib.pyplot as plt
plt.ion()

#Define a model function to use when fitting data.
#  For this example, that's a gaussian function plus a linear offset.
def f(x, p):
    a, b, c, d, e = p
    return a*np.exp(-(x-b)**2/(2*c**2))  +  d*x + e

#Make some fake data with added noise.
npoints = 30
a, b, c, d, e = 5., 1., 2., 0.2, 2.
p = [a, b, c, d, e]
x = np.linspace(-10, 10, npoints)
y = f(x, p)+np.random.normal(0, 0.5, npoints)
x += np.random.normal(0, .05, npoints)

fig, ax = plt.subplots()
ax.scatter(x, y)

mcmc = MCMC(x, y, model=f)
mcmc.add_walkers(1, p0=[1., 1., 1., 1., 1.]) #Starting guess is [1.0, 1.0, 1.0, 1.0, 1.0]
mcmc.walk(200, run_id="burn")
mcmc.add_walkers(4)
mcmc.walk(1000, run_id="walk")