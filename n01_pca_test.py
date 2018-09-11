import numpy as np
from sklearn.decomposition import PCA


def pca_pro():
    """pca降维"""
    pca = PCA(n_components=2)
    X = np.array([[-1, -1, 1, 1], [-2, -1, 1, 1], [-3, -2, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 2, 1, 1]])
    Y = np.array([[-2, -5, 1, 2]])
    print(X)
    print(pca)
    pca.fit(X)
    change_x = pca.transform(X)
    change_y = pca.transform(Y)
    print(change_x)
    print(change_y)


if __name__ == '__main__':
    pca_pro()
