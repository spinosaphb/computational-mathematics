import numpy as np

def jacobi(A, b, x, ITERATION_LIMIT = 1000, precision = 1e-10):

    i = 0
    while i < ITERATION_LIMIT:
        x_new = np.zeros_like (x)
        
        for i in range(A.shape[0]):
            s1 = np.dot(A[i, :i], x[:i])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        
        if np.allclose(x, x_new, atol=precision, rtol=0.):
            break
        
        x = x_new
        i += 1
    error = np.dot(A, x) - b

    return x, error