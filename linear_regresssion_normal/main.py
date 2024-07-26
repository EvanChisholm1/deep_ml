import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    X = np.array(X)
    y = np.array(y).reshape(-1, 1)

    theta = np.linalg.inv(np.transpose(X) @ X) @ np.transpose(X) @ y
    theta = theta.round(4).flatten().tolist()

    return theta

print(linear_regression_normal_equation(X = [[1, 1], [1, 2], [1, 3]], y = [1, 2, 3]))
