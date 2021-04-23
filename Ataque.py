class Ataque:
    def __init__(self, armas):
        self.armas = armas
        self.armasCorretasNaPosicaoCorreta = 0
        self.armasCorretasNaPosicaoErrada = 0

    def __del__(self):
        self.armas = []

    def conferirAtaque(self, defesaDoMonstro):
        count = 0

        for armaDefensiva in defesaDoMonstro:
            if armaDefensiva == self.armas[count]:
                self.acertouAtaque()

            elif armaDefensiva in self.armas:
                self.acertouArma()

            count += 1

        return self.conferirSeGanhou

    def acertouAtaque(self):
        self.armasCorretasNaPosicaoCorreta += 1

    def acertouArma(self):
        self.armasCorretasNaPosicaoErrada += 1

    def conferirSeGanhou(self):
        return self.armasCorretasNaPosicaoCorreta == 4

""" 
- Criacao dos dubles para a classe Ataque
- Testador: Jose Joao
"""
class AtaqueStub(Ataque):
    def __init__(self):
        self.armas = [1,2,3,4]
        self.armasCorretasNaPosicaoCorreta = 0
        self.armasCorretasNaPosicaoErrada = 0

class AtaqueDummy(Ataque):
    pass

class AtaqueSpy(Ataque):
    def __init__(self, armas):
        self.armas = armas
        self.armasCorretasNaPosicaoCorreta = 0
        self.armasCorretasNaPosicaoErrada = 0
        self.acertouAtaqueCount = 0
    
    def __del__(self):
        self.armas = []
        self.armasCorretasNaPosicaoCorreta = 0
        self.armasCorretasNaPosicaoErrada = 0
        self.acertouAtaqueCount = 0

    def acertouAtaque(self):
        self.acertouAtaqueCount += 1