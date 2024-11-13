# Composicao

# Na composicao, o objeto e dono de outro objeto

class ItemNotaFiscal:
    def __init__(self, descricao):
        self.descricao = descricao

# Nesse caso, a classe NotaFiscal, vai ser dona do ItemNotaFiscal

class NotaFiscal:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, descricao):
        item = ItemNotaFiscal(descricao)
        self.itens.append(item)

    def mostrar_itens(self):
        for item in self.itens:
            print(f"Item: {item.descricao}")

# Aqui vai ser uma instancia para criar uma nota fiscal e botar pra exibir

nota = NotaFiscal()
nota.adicionar_item("Produto A")
nota.adicionar_item("Produto B")


nota.mostrar_itens()


# Quando um objeto e deletado ( Se a classe principal for apagada), todos os outos sao

del nota

# NEsse caso, se deletar nota, nao havera nada, pois nao havera itens
