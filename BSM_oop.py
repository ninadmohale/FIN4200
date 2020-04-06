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
            return ((np.log(S/K) + (r + 0.5 * vol**2)*(T-t))/(vol*np.sqrt(T-t)))

        def BS_call(S, K, r, vol, T, t, d1, d2):
            return (S * norm.cdf(d1) - K * np.exp(-r*T)*norm.cdf(d2))

        def BS_put(S, K, r, vol, T, t, d1, d2):
            return (BS_call(S, K, r, vol, T, t, d1, d2) - S + np.exp(-r*(T-t))*K)

        self.d1 = d1_calc(S, K, r, vol, T, t)
        self.d2 = self.d1 - vol * np.sqrt(T)

        if otype == 'call':
            self.price = BS_call(S, K, r, vol, T, t,self.d1,self.d2)
        else:
            self.price = BS_put(S, K, r, vol, T, t,self.d1,self.d2)

        # Greeks
        def delta(S, K, r, vol, T, t, otype, d1, d2):
            if(otype == "call"):
                delta = np.exp(-(T-t))*norm.cdf(d1)
            elif(otype == "put"):
                delta = -np.exp(-(T-t))*norm.cdf(-d1)
            return delta

        def vega(S, K, r, vol, T, t, otype, d1, d2):
            return S * norm.pdf(d1) * np.sqrt(T-t)

        def rho(S, K, r, vol, T, t, otype, d1, d2):
            if(otype == "call"):
                rho = K*(T-t)*np.exp(-r*(T-t))*norm.cdf(d2)
            elif(otype == "put"):
                rho = -K*(T-t)*np.exp(-r*(T-t))*norm.cdf(-d2)
            return rho

        def theta(S, K, r, vol, T, t, otype, d1, d2):
            if(otype == "call"):
                theta = -(S*norm.pdf(d1)*vol / (2*np.sqrt(T-t))) - r*K*np.exp(-r*(T-t))*norm.cdf(d2)
            elif(otype == "put"):
                theta = -(S*norm.pdf(d1)*vol / (2*np.sqrt(T-t))) + r*K*np.exp(-r*(T-t))*norm.cdf(-d2)
            return theta

        def gamma(S, K, r, vol, T, t, otype, d1, d2):
            gamma = (norm.pdf(d1)) / (S * vol * np.sqrt(T-t))
            return gamma

        def charm(S, K, r, vol, T, t, otype, d1, d2):
            charm = -norm.pdf(d1)*(2*r*(T-t) - d2*vol*np.sqrt(T-t))/(2*(T-t)*vol*np.sqrt(T-t))
            return charm

        self.delta = delta(S, K, r, vol, T, t, otype, self.d1, self.d2)
        self.vega = vega(S, K, r, vol, T, t, otype, self.d1, self.d2)
        self.rho = rho(S, K, r, vol, T, t, otype, self.d1, self.d2)
        self.theta = theta(S, K, r, vol, T, t, otype, self.d1, self.d2)
        self.gamma = gamma(S, K, r, vol, T, t, otype, self.d1, self.d2)
        self.charm = charm(S, K, r, vol, T, t, otype, self.d1, self.d2)


a1 = option('call',254,250,0.1,0.2,10,0)

print(type(a1))

print('type',a1.otype)
print('S',a1.S)
print('K',a1.K)
print('vol',a1.vol)
print('r',a1.r)
print('T',a1.T)
print('t',a1.t)
print('d1',a1.d1)
print('d2',a1.d2)

print('price',a1.price)

print('delta',a1.delta)
print('vega',a1.vega)
print('rho',a1.rho)
print('theta',a1.theta)
print('gamma',a1.gamma)
print('charm',a1.charm)
