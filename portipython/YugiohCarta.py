# Criação de Classe e objeto

# Para criar uma classe no python necessita criar um novo arquivo

class YugiohCarta: # A partir disso cria uma classe com o nome do arquivo.

    # Dentro da classe utiliza uma funçao com o nome init
    # Definimos as caracteristicas do objeto, nesse caso, demos o nome, o ataque, a defesa 
    # e Habilidade da carta.

    def __init__(self, nome, ataque, defesa, habilidade):

        self.nome = nome 
        self.ataque = ataque
        self.defesa = defesa
        self.habilidade = habilidade


        # O self vai fazer a referencia a classe criada e vai ajudar a definir as caracteristicas
        # Que criamos.

    def exibirCarta(self):
        print(f'Nome: {self.nome}')
        print(f'Ataque: {self.ataque}')
        print(f'defesa: {self.defesa}')
        print(f'Habilidade: {self.habilidade}')

# Instanciando o objeto fora da classe para definir as caracteristicas
# E retornando a funcao para exibir a carta.

CartaMonstro = YugiohCarta('Luster Dragon', 1900, 1600, 'não tem')
CartaMonstro.exibirCarta()
