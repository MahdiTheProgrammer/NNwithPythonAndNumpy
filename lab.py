import numpy as np
import math

class Vanila:
    """
    In NN class there are different ML models and functions available that helps you build and train your ML model.
    """
    def __init__(self):
        self.layers = []
        self.weights = []
        self.biases = [] 
        self.init_method = None


    def add_vanila(self, number_of_neurons):
        if not isinstance(number_of_neurons, int):
            raise TypeError("The number of neurons must be an integer.")
        if number_of_neurons < 1:
            raise ValueError("The number of neurons must be at least 1.")
        if self.init_method == None:
            raise ValueError("In order to add a layer you have to set the initializtion method")

        if self.layers:
            previous_neurons = self.layers[-1]
            if self.init_method == "xavier":
                weights = np.random.uniform(-(np.sqrt(6/(previous_neurons+number_of_neurons))), np.sqrt(6/(previous_neurons+number_of_neurons))), (previous_neurons, number_of_neurons)
            else:
                weights = np.random.randn(previous_neurons, number_of_neurons) * np.sqrt(2 / previous_neurons) #IDK why

            self.weights.append(weights)
        
        self.biases.append(np.zeros(number_of_neurons,1))
        self.layers.append(number_of_neurons)

    def properties(self):
        print("It is a vanila neural network with "+ str(len(self.layers)) + " layers. The number of neurons are: "+ str(self.layers) + ".")
        if self.init_method is not None:
            print("The initializtion method is: "+ str(self.init_method))

    def set_init_method(self, init_method=""):
        """
        Choose between 'xavier' or 'he' initialization method.
        """
        if init_method == "xavier" or init_method == "he":
            self.init_method = init_method
        else:
            raise ValueError("For vanila model only xavier and he is available at this moment")

class Activations:
    def sigmoid(self, x):
        y = 1 / (1 + np.exp(-x))  
        return y

    def tanh(self, x):
        y = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))  
        return y

    def ReLU(self, x):
        return np.maximum(0, x)  
