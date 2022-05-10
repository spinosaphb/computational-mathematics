import numpy as np

def _seidel(A, x ,b):
    n = len(A)                   
    
    for j in range(0, n):        
        d = b[j]                  
          
        for i in range(0, n):     
            if(j != i):
                d -= A[j][i] * x[i]
        x[j] = d / A[j][j]
    
    return x   

def gauss_seidel(A, x, b, precision=1e-10):
    while True:
        x = _seidel(A, x, b)
        if np.allclose(A, x, atol=precision, rtol=0.):
            break
        print(x)
    return x