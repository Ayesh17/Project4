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
    identity = np.identity(len(cov))
    print(identity)

    # Calculating Eigenvalues and Eigenvectors of the covariance matrix
    eigen_values, eigen_vectors = np.linalg.eigh(cov)
    print("val",eigen_values)
    print("vect",eigen_vectors)


    return 0, 0
