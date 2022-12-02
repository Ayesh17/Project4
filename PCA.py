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
    eigen_values, eigen_vectors = np.linalg.eig(cov)

    n = len(eigen_values)
    indexes = eigen_values.argsort()[::-1][:n]

    eigen_values_sorted = np.empty(shape= len(eigen_values))
    eigen_vectors_sorted = np.empty(shape= (len(eigen_vectors), len(eigen_vectors[0])))
    print("indexes", indexes)
    for i in range(len(indexes)):
        print(indexes[i])
        print(eigen_values[indexes[i]])
        eigen_values_sorted[i] = eigen_values[indexes[i]]
        eigen_vectors_sorted[i] = eigen_vectors[indexes[i]]


    print("val",eigen_values)
    print("vect",eigen_vectors)

    print("indexes", indexes)
    print("val_sorted", eigen_values_sorted)
    print("vect_sorted", eigen_vectors_sorted)

    return eigen_vectors, eigen_values

def project_data(Z, PCS, L):
    print("Z", Z)
    print("PCS", PCS[0])
    print("L", L)
    Z_star = np.matmul(Z , PCS[0])
    print("Z_star", Z_star)
    return Z_star

def show_plot(Z, Z_star):

    # cluster1 = clusters[0]

    ZX = np.zeros(len(Z))
    ZY = np.zeros(len(Z))
    for i in range(len(Z)):
        ZX[i] = Z[i][0]
        ZY[i] = Z[i][1]
    print("ZX",ZX)
    print("ZY",ZY)
    plt.scatter(ZX, ZY, color="blue")

    plt.plot(Z_star, color="black")
    plt.show()
    return 0

