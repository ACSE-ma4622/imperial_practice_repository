import numpy.linalg as la
import numpy as np
from numpy.polynomial import Polynomial
denominators = np.arange(1,10000)
signs = np.ones((denominators.shape[0],))
signs[0:-1:4] = -1
signs = -signs
coeff = signs/denominators
coeff[1:-1:2] = 0
arctan_series = Polynomial(coeff)
print(4*arctan_series(1))







