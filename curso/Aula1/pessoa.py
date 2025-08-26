from datetime import date


class Pessoa:
    ano_atual = int(date.today().year)
    nome: str
    idade: int
    falando: bool
    comendo: bool
    def __init__(self, nome, idade, falando = False, comendo = False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto: str):
        if not self.comendo:
            if not self.falando:
                print(f'{self.nome} está falando sobre {assunto}')
                self.falando = True
            else:
                raise Exception(f'{self.nome} já está falando')
        else:
            raise Exception(f'{self.nome} não pode falar, está comendo!')

    def comer(self, alimento: str):
        if not self.comendo:
            print(f'{self.nome} está comendo {alimento}')
            self.comendo = True
        else:
            raise Exception(f'{self.nome} já está comendo {alimento}')

    def pararDeComer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
        else:
            self.comendo = False