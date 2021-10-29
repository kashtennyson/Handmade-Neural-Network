import numpy as np



def sigmoid(Z):
    
    s = 1/(1 + np.exp(-Z))
    cache = Z
    
    return s, cache



def relu(Z):
    

    r = np.maximum(0, Z)
    cache = Z
    
    return r, cache



def linear_function(Z):

    l = Z
    cache = Z
    
    return l, cache



def sigmoid_backward(dA, cache):
    
    Z = cache
    s = 1/(1 + np.exp(-Z))
    
    dZ = dA * s * (1-s)
    
    return dZ



def relu_backward(dA, cache):
    
    Z = cache
    dZ = np.array(dA, copy = True)
    dZ[Z <= 0] = 0
    
    return dZ



def linear_function_backward(dA, cache):
    
    Z = cache
    dZ = dA
    
    return dZ
    


