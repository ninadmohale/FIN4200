import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # Plotting tools
from scipy.stats import norm # For Black Scholes Model


class option:
    def __init__(self,otype,S,K,vol,r,T,t):
        self.otype = otype
        self.S = S
        self.K = K
        self.vol = vol
        self.r = r
        self.T = T
        self.t = t

        def d1_calc(S, K, r, vol, T, t):
            # Calculates d1 in the BSM equation
            return (np.log(S/K) + (r + 0.5 * vol**2)*(T-t))/(vol*np.sqrt(T-t))

        def BS_call(S, K, r, vol, T, t, d1, d2):
            return S * norm.cdf(d1) - K * np.exp(-r*T)*norm.cdf(d2)

        def BS_put(S, K, r, vol, T, t, d1, d2):
            return BS_call(S, K, r, vol, T, t, d1, d2) - S + np.exp(-r*(T-t))*K

        self.d1 = (np.log(S/K) + (r + 0.5 * vol**2)*(T-t))/(vol*np.sqrt(T-t))
        self.d2 = self.d1 - vol * np.sqrt(T)

        if otype == 'call':
            self.price = BS_call(S, K, r, vol, T, t,self.d1,self.d2)
        else:
            self.price = BS_put(S, K, r, vol, T, t,self.d1,self.d2)





a1 = option('call',254,250,10,2,3,0)

print(a1)


print(a1.otype)
print(a1.S)
print(a1.K)
print(a1.vol)
print(a1.r)
print(a1.T)
print(a1.t)
print(a1.d1)
print(a1.d2)

print(a1.price)

# (otype,S,K,vol,r,T,t)
