class PilhaEstatica():
    def __init__(self):
        self.vetor = [None, None, None, None, None]
        self.quant = 0
        
    def push(self, valor):
        self.vetor[self.quant] = valor
        self.quant += 1

    def pop(self):
        self.quant -= 1

    def getTopo(self):
        return self.vetor[self.quant-1]

    def estaVazia(self):
        return self.quant == 0

    def estaCheia(self):
        return self.quant == 5





    def show(self):
        i = 0
        while i < self.quant:
            print(self.vetor[i])
            i += 1
