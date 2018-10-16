import random
import math

class Neuronio_SOM:
    def __init__(self,size_of_features):
        self.size = size_of_features

    def initRandom(self, randomize_min, randomize_max):
        self.features_vector = [random.uniform(randomize_min,randomize_max) for x in range(self.size)]
    
    def distanceAll(self, features_to_calc):
        # print(self.features_vector)
        soma = 0
        for i in range(self.size):
            soma = soma + math.pow(self.features_vector[i]-features_to_calc[i],2)
        return math.sqrt(soma)

    def update(self, features_to_go, factor):
        for i in range(self.size):
            increase = (features_to_go[i] - self.features_vector[i]) * factor 
            self.features_vector[i] = self.features_vector[i] + increase

    def getFeatures(self):
        return self.features_vector

# Teste Neuronio:
X = Neuronio_SOM(5)
X.initRandom(0.2,0.4)

a = [4,3,2,1,0]
print(X.distanceAll(a))
X.update(a,0.2)
print(X.distanceAll(a))

b = [2,6]
Y = [[Neuronio_SOM(2) for j in range(5)] for i in range(10)]
for i,linha_neuroniio in enumerate(Y):
    for j,neuronio in enumerate(linha_neuroniio):
        neuronio.initRandom(0.3,0.5)
        print(i,j,neuronio.getFeatures())
        print(neuronio.distanceAll(b))
        neuronio.update(b,0.4)
        print(i,j,neuronio.getFeatures())
        print(neuronio.distanceAll(b))
        