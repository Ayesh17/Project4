#imports
import numpy as np
import matplotlib.pyplot as plt

#getting the covariance matrix
def compute_covariance_matrix(Z):
    #Center the data
    mean = np.mean(Z, axis=0)
    Z_centered = np.zeros([len(Z),2])
    for i in range(len(Z)):
        for j in range(len(Z[i])):
            Z_centered[i][j] =  Z[i][j] - mean[j]

    #get the covariance matrix
    ZT = np.transpose(Z_centered)
    cov = np.matmul(ZT, Z_centered)
    return cov

#get PCAs
def find_pcs(cov):
    identity = np.identity(len(cov))

    # Calculating Eigenvalues and Eigenvectors of the covariance matrix
    eigen_values, eigen_vectors = np.linalg.eig(cov)

    #sort eigenvalues and eigenvectors in descending order
    n = len(eigen_values)
    indexes = eigen_values.argsort()[::-1][:n]

    eigen_values_sorted = np.empty(shape= len(eigen_values))
    eigen_vectors_sorted = np.empty(shape= (len(eigen_vectors), len(eigen_vectors[0])))
    for i in range(len(indexes)):
        eigen_values_sorted[i] = eigen_values[indexes[i]]
        eigen_vectors_sorted[i] = eigen_vectors[indexes[i]]

    print("vect", eigen_vectors_sorted)
    print("val", eigen_values_sorted)

    return eigen_vectors_sorted, eigen_values_sorted

#project the data
def project_data(Z, PCS, L):
    Z_star = np.matmul(Z , PCS[0])
    return Z_star

#plot the graph
def show_plot(Z, Z_star):
    ZX = np.zeros(len(Z))
    ZY = np.zeros(len(Z))
    for i in range(len(Z)):
        ZX[i] = Z[i][0]
        ZY[i] = Z[i][1]

    #projected data
    Z_star_y = np.zeros((len(Z_star)))
    plt.scatter(Z_star, Z_star_y, color="red")

    #original data
    plt.scatter(ZX, ZY, color="blue")

    plt.show()
    return 0

