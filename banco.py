class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial

    def __str__(self):
        return f"{self.titular}: {self.saldo}"

class Banco:
    def __init__(self):
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def buscar_conta(self, titular):
        for conta in self.contas:
            if conta.titular == titular:
                return conta
        return None

    def listar_contas(self):
        return sorted(self.contas, key=lambda conta: conta.saldo)

# Exemplo de uso:
banco = Banco()
banco.adicionar_conta(ContaBancaria("João", 500))
banco.adicionar_conta(ContaBancaria("Maria", 1500))
banco.adicionar_conta(ContaBancaria("Carlos", 300))

conta = banco.buscar_conta("maria")
if conta:
    print(f"Conta encontrada: {conta}")
else:
    print("Conta não encontrada.")

for conta in banco.listar_contas():
    print(conta)
