#Decay Rate Coefficients
import numpy as np
t12=np.array([3.8879e+08, 8.3800e-01, 7.7000e-01, 2.0200e-02, 1.2231e+03, 1.7988e+11, 1.1000e-02, 5.9790e+02, 7.0606e+01, 1.2224e+02]) #Half-lives for H3, Li8, B12, C14, B8, C11, N12, N13, O14, and O15 respectively
l=(np.log(2))/t12 #decay coefficient lambda
print l