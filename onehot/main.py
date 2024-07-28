import numpy as np

def to_categorical(x: np.ndarray, n_col=None):
    n_col = n_col if n_col is not None else x.max() + 1
    out = np.zeros((x.shape[0], n_col))

    for i, c in enumerate(x.tolist()):
        out[i, c] = 1
    
    return out


print(to_categorical(np.array([0, 1, 2, 1, 0])))