#imports
import numpy as np
import matplotlib.pyplot as plt

#getting the covariance matrix
def compute_covariance_matrix(Z):
    ZT = np.transpose(Z)
    cov = np.matmul(ZT, Z)
    print(cov)
    return cov

def find_pcs(cov):
    return 0, 0