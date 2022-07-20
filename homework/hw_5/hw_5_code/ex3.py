import numpy as np
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression


def find_columns(sensor):
    pca = PCA()
    pca.fit(sensor)

    for i in range(len(pca.explained_variance_ratio_.round(2))):
        val = pca.explained_variance_ratio_.round(2)[i]
        if val - 0.01 > 0:
            print("column {}: {}".format(i, val))


def linear_fit(sensor):
    x = sensor[:, :3]
    y = sensor[:, -1]
    reg = LinearRegression().fit(x, y)
    print("Coefficient:", reg.coef_)
    print("Intercept:", reg.intercept_)
    print("R_square:", reg.score(x, y))


if __name__ == '__main__':
    for csv in "sensors1.csv", "sensors2.csv":
        print(" ---------- {} ----------".format(csv))
        sensor = np.loadtxt(open(csv, "rb"), delimiter=',')
        find_columns(sensor)
        linear_fit(sensor)
