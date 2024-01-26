class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria 
        self.ativo = False

sushi = Restaurante('Sushi', 'Japonesa')

pizzaria = Restaurante('Pizzaria', 'Italiana')

restaurantes = [sushi, pizzaria]

print(restaurantes)