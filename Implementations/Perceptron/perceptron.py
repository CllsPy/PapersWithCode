import numpy as np


class Perceptron:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.bias = None
        self.weights = None
    
    def _step_function(self, x, threshold: int = 0):
        return np.where(x > threshold, 1, 0)
    
    def fit(self, X, y):
        n_samples, n_featues = X.shape

        self.weights = np.zeros(n_featues)
        self.bias = 0

        for _ in range(n_iterations):
            for i in range(n_samples):
                z = np.dot(X[i], self.weights) + self.bias
            
            #  apply activation function
            y = self._step_function(z)

            #  update w and b
            self.weights += self.learning_rate * (y[i] - y_pred) * X[i)
            self.bias += self.learning_rate * (y[i] - y_pred)
