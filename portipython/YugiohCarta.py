# Criação de Classe

# Para criar uma classe 

class YugiohCarta:

    def __init__(self, nome, ataque, defesa, habilidade):

        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
        self.habilidade = habilidade

        CartaMonstro = YugiohCarta('Luster Dragon', 1900, 1600, 'Nao tem')
