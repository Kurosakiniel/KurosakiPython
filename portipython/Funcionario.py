# encapsulamento

# O encapsulamento ajuda na proteção dos dados, ele ajuda para nao ter alteracoes em outras classes ou ate
# Na mesma classe

class Funcionario:

    def __init__(self, nome, cargo, ValorPorHoraTrabalhada):
    
        self.nome = nome
        self.cargo = cargo
        self.ValorPorHoraTrabalhada = ValorPorHoraTrabalhada
        self.__HorasTrabalhadas = 0 # Usando underscore para não poder usar os dados fora ca classe
        self.__salario = 0

    # O uso do underscore ainda pode permitir  que os dados sejam alterados, então nesse caso é necessario
    # Usar o @propriety.

    @property
    def salario(self): 
        return self.__salario

    @salario.setter
    def salario(self, novo_salarioi):
        raise ValueError("Impossivel alterar salario de forma direta. Use a funcao calcularSalario().")

    def registroHorasTrabalhadas(self):

        self.HorasTrabalhadas += 1
    
    def calcularSalario(self):
        self.salario = self.HorasTrabalhadas * self.ValorPorHoraTrabalhada
