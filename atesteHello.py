import unittest

# esperado = int(input("Digite o valor esperado do teste: "))  # valor esperado do teste
esperado = input("Digite o valor esperado do teste: ")  # valor esperado do teste
# definir = 2*2
definir = "Valor a Ser Testado"

def programa_ser_testado():  # função a ser testada
    # return int(definir) # define o valor retornado pela função
    return (definir) # define o valor retornado pela função


class nomeClasseTeste(unittest.TestCase):
    def teste_programa(self):
        resultado = programa_ser_testado()  # chamada da função a ser testada
        self.assertEqual(resultado, esperado)  # comparação do resultado com o esperado

if __name__ == '__main__':
    unittest.main()


