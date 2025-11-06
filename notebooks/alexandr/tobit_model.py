import pandas as pd
import numpy as np
from scipy import stats, linalg
from scipy.stats import norm
from scipy.optimize import minimize
from sklearn.linear_model import LinearRegression
from scipy.sparse import issparse

class TobitModel:
    def __init__(self, ul=np.inf, lol=-np.inf): 
        #self.X = X    # Independent variables
        #self.y = y    # Dependent variable
        self.ul = ul  # Upper limit for censoring
        self.lol = lol  # Lower limit for censoring
        self.params_ = None # Placeholder for estimated parameters

    def tobit_ll(self, par):
        '''Computes negative log likelihood as a function of the parameters'''
        X = self.X
        y = self.y
        ul = self.ul
        lol = self.lol
        
        # Extract parameters
        sigma = np.exp(par[-1])
        beta = par[:-1]
        
        indicator_up = (y >= ul)
        indicator_mid = (y > lol) & (y < ul)
        indicator_down = (y <= lol)
        # Linear predictor
        if issparse(X):
            lp = np.dot(X.todense(),beta).reshape(np.shape(y))
        else:
            lp = np.dot(X, beta)
        
        # A small epsilon to prevent log(0)
        eps = 1e-10

        #print('Size of y = ',np.shape(y),', size of lp = ',np.shape(lp),' size of beta = ',np.shape(beta),', and X = ',np.shape(X))
        # Compute likelihood parts, clipping to avoid log(0)
        ll_obs = np.log(np.clip((1/sigma) * norm.pdf((y - lp) / sigma), eps, None))
        ll_cens_above = np.log(np.clip(1 - norm.cdf((ul - lp) / sigma), eps, None))
        ll_cens_below = np.log(np.clip(1 - norm.cdf((lp - lol) / sigma), eps, None))
        
        ll = np.sum(indicator_down * ll_cens_below) + np.sum(indicator_mid * ll_obs) + np.sum(indicator_up * ll_cens_above)
        return -ll
        
    def fit(self,X,y):
        """Fit the Tobit model using maximum likelihood estimation."""
        self.X = X
        self.y = y

        num_params = self.X.shape[1] + 1  # Number of parameters (beta + sigma)
        
        # Initialize the parameters with OLS linear regression model parameters
        lr = LinearRegression(fit_intercept=False)
        lr.fit(self.X, self.y)
        params = list(lr.coef_)

		# added from https://stackoverflow.com/questions/27928275/find-p-value-significance-in-scikit-learn-linearregression
        #params2 = np.append(lr.intercept_,lr.coef_)
        params2 = lr.coef_
        pred = lr.predict(self.X)
        newX = X
        #newX = np.append(np.ones((len(X),1)),self.X,axis=1)
        if issparse(X):
            MSE = (sum((self.y-pred)**2))/(newX.shape[0]-newX[0].shape[0])
            self.var_b = MSE*(np.linalg.inv(np.dot(newX.todense().T,newX.todense())).diagonal())
            self.sd_b = np.sqrt(np.abs(self.var_b))
            self.ts_b = params2/ self.sd_b
            self.p_values =np.append(0,[2*(1-stats.t.cdf(np.abs(i),(newX.shape[0]-newX[0].shape[0]))) for i in self.ts_b])
        else:
            MSE = (sum((self.y-pred)**2))/(len(newX)-len(newX[0]))
            self.var_b = MSE*(np.linalg.inv(np.dot(newX.T,newX)).diagonal())
            self.sd_b = np.sqrt(self.var_b)
            self.ts_b = params2/ self.sd_b
            self.p_values =[0]+[2*(1-stats.t.cdf(np.abs(i),(len(newX)-len(newX[0])))) for i in self.ts_b]

        # Compute sigma from residuals and ensure it is not too small
        residual_std = np.sqrt(np.sum((self.y - lr.predict(self.X))**2) / len(self.y))
        sigma = residual_std * 1.5
        sigma = max(sigma, 1e-5)  # Enforce a lower bound for sigma
        params.append(np.log(sigma))
        self.params_ = params

        # Correct bounds: for the log(sigma) parameter, lower bound should be log(1e-5)
        bounds = [(None, None)] * len(params[:-1]) + [(np.log(1e-5), None)]
        
        # Minimize the negative log likelihood
        result = minimize(self.tobit_ll, self.params_, method='L-BFGS-B', bounds=bounds, 
                          options={'maxiter': 10000, 'ftol': 1e-10})
        self.params_ = result.x  # Store the optimized parameters

    def predict(self, X_new):
        """
        Predict the latent variable values for new data.
        """
        if self.params_ is None:
            raise ValueError("Model is not fitted yet. Please call the fit method first.")

        beta = self.params_[:-1]         # Coefficients
        sigma = np.exp(self.params_[-1])   # Standard deviation
        
        # Linear predictor
        if issparse(X_new):
            lp = np.dot(X_new.dense(),beta)
        else:
            lp = np.dot(X_new, beta)
        return lp  # Return the predicted latent variable values
