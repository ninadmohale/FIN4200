# -*- coding: utf-8 -*-
"""
Option Pricing

https://www.optionseducation.org/toolsoptionquotes/optionscalculator  (to check answers)

"""


def bsmprice(putOrCall: 'P-put or C-call', undlyPx: 'Underlying Price' ,strikePx: 'Strike Price' ,t: 'Time to maturity in years',vol: 'Volatility', r: 'Risk Free Rate'):
    from math import log,sqrt,exp
    from scipy.stats import norm
    nd=norm(0.0,1.0)
    d1=(log(undlyPx/strikePx)+(r+vol*vol/2)*t)/(vol*sqrt(t))
    d2=d1-vol*sqrt(t)
    if putOrCall == "C":
        px=undlyPx*nd.cdf(d1)-strikePx*exp(-r*t)*nd.cdf(d2)
    elif putOrCall=="P":
        px=strikePx*exp(-r*t)*nd.cdf(-d2)-undlyPx*nd.cdf(-d1)
    else:
        px=-99.0          
    return px

def delta(putOrCall: 'P-put or C-call', undlyPx: 'Underlying Price' ,strikePx: 'Strike Price' ,t: 'Time to maturity in years',vol: 'Volatility', r: 'Risk Free Rate'):
    from math import log,sqrt
    from scipy.stats import norm
    nd=norm(0.0,1.0)
    d1=(log(undlyPx/strikePx)+(r+vol*vol/2)*t)/(vol*sqrt(t))
    if putOrCall == "C":
        delta=nd.cdf(d1)
    elif putOrCall=="P":
        delta=nd.cdf(d1)-1
    else:
        delta=-99.0          
    return delta

def gamma(undlyPx: 'Underlying Price' ,strikePx: 'Strike Price' ,t: 'Time to maturity in years',vol: 'Volatility', r: 'Risk Free Rate'):
    from math import log,sqrt
    from scipy.stats import norm
    nd=norm(0.0,1.0)
    d1=(log(undlyPx/strikePx)+(r+vol*vol/2)*t)/(vol*sqrt(t))
    gamma=nd.pdf(d1) / (undlyPx*vol*sqrt(t))
    return gamma

def vega(undlyPx: 'Underlying Price' ,strikePx: 'Strike Price' ,t: 'Time to maturity in years',vol: 'Volatility', r: 'Risk Free Rate'):
    from math import log,sqrt
    from scipy.stats import norm
    nd=norm(0.0,1.0)
    d1=(log(undlyPx/strikePx)+(r+vol*vol/2)*t)/(vol*sqrt(t))
    vega=undlyPx * nd.pdf(d1) * sqrt(t)
    return vega / 100.0

def rho(putOrCall: 'P-put or C-call', undlyPx: 'Underlying Price' ,strikePx: 'Strike Price' ,t: 'Time to maturity in years',vol: 'Volatility', r: 'Risk Free Rate'):
    from math import log,sqrt,exp
    from scipy.stats import norm
    nd=norm(0.0,1.0)
    d1=(log(undlyPx/strikePx)+(r+vol*vol/2)*t)/(vol*sqrt(t))
    d2=d1-vol*sqrt(t)
    if putOrCall == "C":
        rho=strikePx*t*exp(-r*t)*nd.cdf(d2)
    elif putOrCall=="P":
        rho=-strikePx*t*exp(-r*t)*nd.cdf(-d2)
    else:
        rho=-99.0 
    return rho

def theta(putOrCall: 'P-put or C-call', undlyPx: 'Underlying Price' ,strikePx: 'Strike Price' ,t: 'Time to maturity in years',vol: 'Volatility', r: 'Risk Free Rate'):
    from math import log,sqrt,exp
    from scipy.stats import norm
    nd=norm(0.0,1.0)
    d1=(log(undlyPx/strikePx)+(r+vol*vol/2)*t)/(vol*sqrt(t))
    d2=d1-vol*sqrt(t)
    t1= (-undlyPx * nd.pdf(d1) * vol) / (2 * sqrt(t))
    t2= r*strikePx*exp(-r*t)
    if putOrCall == "C":
        theta=t1-t2*nd.cdf(d2)
    elif putOrCall=="P":
        theta=t1+t2*nd.cdf(-d2)
    else:
        theta=-99.0 
    return theta

optionType="C"
stockprice=100.
K=85.00
TimeToExp=90/365.25
vol=.20
rfr=0.010519

tpx=bsmprice("C",stockprice,K,TimeToExp,vol,rfr)
print("theoretical option price test 0=",tpx)

tdelta=delta("C",stockprice,K,TimeToExp,vol,rfr)
print("option delta=",tdelta) 
 
tgamma=gamma(stockprice,K,TimeToExp,vol,rfr)
print("option gamma=",tgamma)  
 
tvega=vega(stockprice,K,TimeToExp,vol,rfr)
print("option vega=",tvega)

trho=rho(optionType,stockprice,K,TimeToExp,vol,rfr)
print("option rho=",trho)

ttheta=theta(optionType,stockprice,K,TimeToExp,vol,rfr)
print("option theta=",ttheta)

tpx1=bsmprice(putOrCall="C",undlyPx=stockprice,strikePx=K,t=0.5,vol=.35,r=.0125)
print("theoretical option price test 1=",tpx1)

tpx2=bsmprice(putOrCall="C",strikePx=85.0,undlyPx=65.0,t=1.0,r=0.02,vol=.20)
print("theoretical option price test 2=",tpx2)

tpx3=bsmprice("P",100.0,75.0,0.25,.20,.0125)
print("theoretical option price test 3=",tpx3)

# tpx4=bsmprice()