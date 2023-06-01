class conta:
    def __init__(self, nome_titular, saldo):
        self.nome_titular = nome_titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"{self.nome_titular}, você depositou: R$ {valor}")

    def sacar(self, valor):
        if self.saldo < valor:
            print(f"Você não tem saldo o suficiente, seu saldo é de: R${self.saldo}")
        else:
            self.saldo -= valor
            print(f"{self.nome_titular}, você sacou: R${valor}")
            lista.append(f'Saque de R$ {valor}')

    def extrato(self, operacoes):
        self.operacoes = operacoes
        if not lista:
            print("Nenhuma operação até o momento.")
        else:
            print(f"{self.nome_titular}, seu extrato é: {operacoes}")

    def valor(self):
        print(f"{self.nome_titular}, seu saldo é de: R${self.saldo}")


pessoa = conta("Carlos", 0.00)
lista = []


def repeat():
    menu = input('''
    O que deseja fazer:
    0.sair
    1.deposito
    2.saque
    3.extrato
    4.saldo
    ''')

    match menu:
        case "0":
            print("Obrigado pela preferência, volte sempre")
            return
        case "1":
            valor_deposito = float(input("Qual o valor do depósito?"))
            pessoa.depositar(valor_deposito)
            lista.append(f'Depósito de R$ {valor_deposito}')

        case "2":
            valor_saque = float(input("Qual o valor do saque?"))
            pessoa.sacar(valor_saque)
        case "3":
            pessoa.extrato(lista)
        case "4":
            pessoa.valor()
        case _:
            print("Por favor escolha uma das opções")
    repeat()


repeat()
