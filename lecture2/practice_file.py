import numpy.linalg as la
import numpy as np
from numpy.polynomial import Polynomial
"""denominators = np.arange(1,10000)
signs = np.ones((denominators.shape[0],))
signs[0:-1:4] = -1
signs = -signs
coeff = signs/denominators
coeff[1:-1:2] = 0
arctan_series = Polynomial(coeff)"""
def finding_number_of_terms(required_accuracy,starting_number_of_terms):
     number_of_terms = starting_number_of_terms
     diff = np.inf
     while diff>required_accuracy:
         denominators = np.arange(1, number_of_terms)
         signs = np.ones((denominators.shape[0],))
         signs[0:-1:4] = -1
         signs = -signs
         coeff = signs / denominators
         coeff[1:-1:2] = 0
         arctan_series = Polynomial(coeff)
         diff = abs(4*arctan_series(1)-np.pi)
         number_of_terms *= 1.0001
     return number_of_terms/1.0001

def approximating_pi(ntot):
    x = np.random.ranf(ntot)
    y = np.random.ranf(ntot)
    sum = x**2+y**2
    sum = sum//1
    nin = np.where(sum ==0)
    ratio = len(nin[0])/ntot
    pi = 4*ratio
    return pi








