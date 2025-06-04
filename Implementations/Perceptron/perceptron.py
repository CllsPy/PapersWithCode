class Perceptron:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.bias = None
        self.weights = None
    
    def activation_function(self, x, thershold: int = 0):
        return np.where(x > thershold, 1, 0)


        
    
x = [1, 2, 3, -1]

neuron = Perceptron()
neuron.activation_function(x)

print((lambda x: x**2)(10))