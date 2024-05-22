class Pessoa():
    def __init__(self, nome, peso, idade, comendo=False, falando=False):  # atributos
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.falando = False

    def comer(self, alimento):  # metodos4
        if self.falando == True:
            print(f"{self.nome} está falando, logo, não pode comer")
        if self.comendo == False:
            print(f"{self.nome} está comendo {alimento}")
            self.comendo = True
        else:
            print(f"{self.nome} já está comendo")

    def pararDeComer(self, alimento):  # metodos
        if self.comendo == True:
            print(f"{self.nome} terminou de comer {alimento}")
            self.comendo = False
        else:
            print(f"{self.nome} já não está comendo nada")
        self.comendo = False

    def falar(self, falas):  # metodos
        if self.falando == False:
            print(f"{self.nome} está falando que: {falas}")
            self.falando == True
        else:
            print(f"{self.nome} já está falando")

    def andar(self, km):  # metodos
        print(f"{self.nome} vai andar {km}km")


class ContaBancaria():
    def __init__(self, numConta, nomeCliente, tipoConta, ):
        self.numConta = numConta
        self.saldo = 0
        self.nomeCliente = nomeCliente
        self.tipoConta = tipoConta
        self.status = False

    def mostrarSaldo(self):
        if self.status == True:
            print(f"{self.nomeCliente} seu saldo é de {self.saldo}R$")
        else:
            print(f"conta inativa")

    def ativarConta(self):
        if self.status == False:
            print(f"{self.nomeCliente} sua conta acabou de ser ativada")
            self.status = True
        else:
            print(f"a conta de {self.nomeCliente} já está ativa")

    def desativarConta(self):
        if self.status == True:
            if self.saldo > 0:
                print(f"{self.nomeCliente} sua conta possui saldo, saque-o para desativa-lá")
            else:
                print(f"{self.nomeCliente} sua conta acabou de ser desativada :/")
                self.status = False
        else:
            print(f"a conta de {self.nomeCliente} já está desativada")

    def depositar(self, valor):
        if self.status == True:
            self.saldo = self.saldo + valor
            print(f"{self.nomeCliente} você acabou de depositar {valor}R$ com sucesso!")
        else:
            print("conta inativa")

    def sacar(self, valor):
        if self.status == True:
            if self.saldo > 0:
                if valor <= self.saldo:
                    print(f"{self.nomeCliente} você acabou de sacar {valor}R$ de sua conta")
                    self.saldo = self.saldo - valor
                else:
                    print(f"Não é possivel sacar {valor}R$, saldo insuficiente")
            else:
                print(f"{self.nomeCliente} sua conta está zerada")
        else:
            print("conta inativa")


class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self, sarro):
        print(f"{self.nome} foi comer {sarro}")


class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def miar(self):
        print(f"{self.nome} foi miar por ai, miau miau")

    def padeiro(self):
        print(f"{self.nome} está amassando pãozinho, a padaria está a todo vapor, que fofo!")


class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def latir(self):
        print(f"{self.nome} latiu... MUITO")


class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def pular(self):
        print(f"{self.nome} pulou por ai... de forma indefinida")


class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def mugir(self):
        print(f"{self.nome} mugiu...muuuh")


class Forma():
    def __init__(self):
        self.area = 0
        self.perimetro = 0


class Retangulo(Forma):
    def __init__(self):
        super().__init__()

    def calcularArea(self, base, altura):
        self.area = base * altura
        print(f"foi calulado a área do retangulo com base: {base} e altura: {altura}")
        print(f"o resultado foi de {self.area}")

    def calcularPerimetro(self, base, altura):
        self.perimetro = 2 * (base + altura)
        print(f"foi calulado o perimetro do retangulo com base: {base} e altura: {altura}")
        print(f"o resultado foi de {self.perimetro}")


class Triangulo(Forma):
    def __init__(self):
        self.altura = 0
        super().__init__()

    def calcularArea(self, lado, altura):
        self.altura = altura
        self.area = (lado * self.altura) / 2
        print(f"foi calulado a área do triangulo com base: {lado} e altura: {self.altura}")
        print(f"o resultado foi de {self.area}")

    def calcularPerimetro(self, lado):
        self.perimetro = lado * 3
        print(f"foi calulado o perimetro do triangulo com lado: {lado}")
        print(f"o resultado foi de {self.perimetro}")


class Atleta():
    def __init__(self,peso):
        self.aposentado = False
        self.peso = 0
        self.parado = False
        self.aquecido = False

    def aposentar(self):
        if self.aposentado == True:
            print(f"o atleta já está aposentado")
        else:
            print(f"o atleta agora está aposentado")
            self.aposentado = True

    def aquecer(self):
        if self.aquecido == True:
            print(f"o atleta já está aquecido")
        else:
            print(f"o atleta foi aquecer...")
            self.aquecido = True

    def parar(self):
        if self.parado == True:
            print("o atleta já está parado")
        else:
            if self.aposentado == True:
                print("o atleta parou")
                self.parado == True
            else:
                print("o atleta está aposentado e não pode aquecer")


class Corredor(Atleta):
    def __init__(self,peso):
        super().__init__(peso)
        self.correndo = False

    def correr(self):
        if self.correndo == True:
            print("O atleta ja está correndo")
        else:
            if self.aquecido == True:
                print("o atleta foi correr")
                self.correndo = True
            else:
                print("é necessario aquecer antes de começar a correr")
    def pararDeCorre(self):
        if self.correndo == False:
            print("já não está correndo")
        else:
            print("atleta parou de correr")
            self.correndo = False
class Nadador(Atleta):
    def __init__(self, peso):
        super().__init__(peso)
        self.nadando = False

    def nadar(self):
        if self.nadando == True:
            print("O atleta ja está nadando")
        else:
            print("o atleta foi nadar")
            self.nadando = True


class Ciclista(Atleta):
    def __init__(self,peso):
        super().__init__(peso)
        self.pedalando = False

    def pedalar(self):
        if self.pedalando == True:
            print("O atleta ja está pedalando")
        else:
            print("o atleta foi nadar")
            self.pedalando = True
