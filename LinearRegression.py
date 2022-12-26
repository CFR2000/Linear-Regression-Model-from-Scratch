import numpy as np



# *** An optimization algorithm is used to update the model's parameters        *** #
# *** in order to minimize the loss.  Common optimization algorithms for linear *** #
# *** regression include gradient descent and stochastic gradient descent.      *** #

class LinearRegression:
    def __init__(self, x, y):
        self.data = x
        self.label = y
        self.m = 0
        self.b = 0
        self.n = len(x)
        pass



    # '''The forward pass involves using the model's parameters to make predictions on the training data.'''
    def fit(self, epochs, lr):

        # Implementing gradient descent
        for i in range(epochs):
            y_pred = self.m*self.data*self.b

            #Calculating derivatives w.r.t Parameters
            D_m = (-2/self.n)*sum(self.data * (self.label - y_pred))
            D_b = (-1/self.n)*sum(self.label-y_pred)


            #Updating Parameters
            self.m = self.m - lr * D_m
            self.c = self.b - lr * D_c



    def predict(self , inp):
        y_pred = self.m * inp + self.b 
        return y_pred


    