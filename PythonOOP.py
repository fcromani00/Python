class Carro:
    def __init__(self, modelo, ano, placa, cor,motor):
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.cor = cor
        self.motor = motor
    def acelerar(self):
        print(f'Pisando no acelerador da {self.modelo}')
        print(f'Subindo a marcha da {self.modelo}')
    def frear(self):
        print (f'Pisando no freio da {self.modelo}')
        print(f'Diminuindo a marcha da {self.modelo}')
    def seta(self):
        print('Sinalizando lado')
    def re(self):
        print('Acionando a Ré no câmbio')
        print('Pisando no acelerador e dando Ré')
    def exibirDados(self):
        print(f'Modelo: {self.modelo}')
        print(f'Ano: {self.ano}')
        print(f'Placa: {self.placa}')
        print(f'Cor: {self.cor}')
        print(f'Motor: {self.motor}\n')

class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
    def dirigirCarro(self, Carro):
        print(self.nome, f'está dirigindo o {Carro.modelo}')
    def fazerCarinho(self, Cachorro):
        print(self.nome, f'está fazendo carinho na {Cachorro.nome}')

class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade
    def latir(self):
        print('Au-au')
    def dormir(self):
        print('Zzzzz...')

meucarro1 = Carro('Gol', 2013,'OLS-9868','Prata',1.0)
meucarro2 = Carro('Doblô', 2012, 'OMA-2317', 'Prata', 1.8)

cachorro1 = Cachorro('Minnie', 'Dachshund', 15)

pessoa1 = Pessoa('Felipe Christofaro Romani', 22, 1.79, 76)
pessoa2 = Pessoa('Rafael Christofaro Romani', 21, 1.77, 78)
pessoa3 = Pessoa('Rubens Romani', 60, 1.72, 85)
pessoa4 = Pessoa('Silene Christofaro Romani', 58, 1.65, 81)
pessoa5 = Pessoa('Ana Paula Christofaro Romani', 20, 1.58, 48)
pessoa6 = Pessoa('João Pedro Christofaro Romani', 25, 1.72, 87)
pessoa7 = Pessoa('Livia Christofaro', 41, 1.50, 79)


pessoa1.dirigirCarro(meucarro1)
meucarro1.acelerar()
meucarro1.frear()
meucarro1.exibirDados()


pessoa4.fazerCarinho(cachorro1)


