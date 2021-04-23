"""
Tudo foi testado com python3
obs: Funcao gerar defesa nao funciona com Python3 na forma que esta
"""

from Ataque import *
import unittest

class AtaqueTestes(unittest.TestCase):

    """ 
    - Criacao dos metodos: 
        - setUp
        - tearDown
        - teste_acertouAtaque_whenAtacar_givenAtaqueCorreto_thenAcertouAtaque,
        - teste_acertouArma_whenAtacar_givenUmaArmaCorret1_thenAcerteArma
    - Testador: Jose Joao
    """

    def setUp(self):
        self.sut = Ataque([1,2,3,4])
    
    def tearDown(self):
        del self.sut
    
    def teste_acertouAtaque_whenAtacar_givenAtaqueCorreto_thenAcertouAtaque(self):
        #given
        self.sut = AtaqueSpy([1,2,3,4])

        #when
        self.sut.conferirAtaque([1,2,3,4])

        #then
        self.assertNotEqual(self.sut.acertouAtaqueCount, 0)
    
    def teste_acertouArma_whenAtacar_givenUmaArmaCorret1_thenAcerteArma(self):
        #given
        self.sut = AtaqueStub()

        #when
        self.sut.conferirAtaque([5,1,6,7])

        #then
        self.assertEqual(self.sut.armasCorretasNaPosicaoErrada, 1)

    """ 
    - Criacao dos metodos: 
        - teste_ganhar_whenAtacar_givenArmasCorretasPosicoesCorretas_thenGanhou
    - Testador: Grimberg
    """

    def teste_ganhar_whenAtacar_givenArmasCorretasPosicoesCorretas_thenGanhou(self):
        # given
        self.sut = AtaqueStub()
        # when
        self.sut.conferirAtaque([1, 2, 3, 4])
        # then
        self.assertTrue(self.sut.conferirSeGanhou())

    """ Questão desafio: 
    - Erro: conferirAtaque retorna self.conferirSeGanhou
    - Solução: Retornar self.conferirSeGanhou()

    - Criacao dos metodos: 
        - teste_ganhar_whenAtacar_givenArmasCorretasPosicoesCorretas_thenGanhou
    - Testadores: Jose Joao e Grimberg
    """

    def test_conferirAtaqque_givenArmasErradas_whenConferirataque_thenConferirAtaqueFalso(self):
        # given : possui armas [1,2,3,4]
        self.sut = AtaqueStub() 

        #when : monstro com defesa diferente, ou seja, armas de ataque erradas
        result = self.sut.conferirAtaque([1,5,3,4])

        #then: esperado um retorno falso
        self.assertFalse(result) 

if __name__ == '__main__':
    unittest.main(verbosity=2)