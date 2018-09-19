from random import uniform
class NeuronioPerceptron:
    def __init__(self, tamanhoentrada):
        self.tam = tamanhoentrada
        self.pesos = [None]*tamanhoentrada
        for i in range(0,self.tam):
            self.pesos[i] = uniform(0,0.1)

    def reset(self, tamanhoentrada):
        self.tam = tamanhoentrada
        self.pesos = [None]*self.tam
        for i in range(0,self.tam):
            self.pesos[i] = uniform(-0.01,0.01)
    
    def metodoAgregacao(self, entrada, peso):
        return entrada*peso

    def novaEntrada(self, entrada):
        if(len(entrada) != self.tam):
            return None
        self.soma = 0
        for i in range(0,self.tam):
            self.soma = self.soma + self.metodoAgregacao(entrada[i], self.pesos[i])
        return self.soma

    def funcaoAtivacao(self):
        if self.soma == None:
            return None
        if(self.soma > 0):
            return 1
        else:
            return 0
    
    def entrada_resultado(self, entrada):
        self.novaEntrada(entrada)
        return self.funcaoAtivacao()