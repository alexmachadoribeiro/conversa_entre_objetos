# NOTE: importando biblioteca
import random

# NOTE: cria a classe
class Pessoa:
    # os atributos são SEMPRE definidos dentro do método construtor
    # método construtor
    def __init__(self, nome, humor):
        self.nome = nome
        self.humor = humor

    # métodos de ação
    def cumprimentar(self):
        if self.humor:
            print(f'Olá, meu nome é {self.nome}. Qual seu nome?')
        else:
            print(f'Tá olhando o quê? Se toca....')
    
    def responder(self, nome, humor):
        if humor:
            print(f'Olá {nome}, meu nome é {self.nome}. Prazer em te conhecer.')
            self.humor = True
        else:
            print(f'Vai se lascar, infeliz.')
            self.humor = False
        return self.humor

# NOTE: programa principal
if __name__ == '__main__':
    humores = (True, False)
    nome1 = input('Informe o nome do 1º usuário: ')
    nome2 = input('Informe o nome do 2º usuário: ')

    # instancia dos objetos
    usuario1 = Pessoa(nome1, humores[random.randint(0,1)])
    usuario2 = Pessoa(nome2, humores[random.randint(0,1)])

    usuario1.cumprimentar()
    usuario1.humor = usuario2.responder(usuario1.nome, usuario2.humor)

    if usuario1.humor:
        print(f'{usuario1.nome} ficou feliz.')
    else:
        print(f'{usuario1.nome} ficou triste.')