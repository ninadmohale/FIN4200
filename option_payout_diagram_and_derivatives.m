% OPTION PAYOUT DIAGRAM and DERIVATIVES

% Put/Call, Strike Price, American/European, Volatility, Expiration Date, Risk-Free Rate
% Option Payout Diagram and Derivatives: Delta, Gamma, Vega, Theta, and Rho

% ASK put/call
strike_price = 45; % ASK
size = 1; % ASK
qty = size*100;
initial_price = 2.88; % ASK
Underlying_price = 30:1:60; % ASK


cashflow_expiration = ((max(Underlying_price-strike_price,0))-initial_price) * qty;


plot(Underlying_price,cashflow_expiration)



