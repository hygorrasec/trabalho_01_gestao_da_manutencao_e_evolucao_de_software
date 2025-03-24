class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular
        self.__saldo = saldo_inicial

    def __str__(self):
        return f"{self.__titular}: {self.__saldo}"

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, novo_saldo):
        if novo_saldo >= 0:
            self.__saldo = novo_saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return True
        return False

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            return True
        return False

    def transferir_para(self, destino, valor):
        if self.sacar(valor):
            destino.depositar(valor)
            return True
        return False


class Banco:
    def __init__(self):
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def buscar_conta(self, titular):
        for conta in self.contas:
            if conta.get_titular().lower() == titular.lower():
                return conta
        return None

    def listar_contas(self):
        return sorted(self.contas, key=lambda conta: conta.get_saldo())

    def saldo_total(self):
        return sum(conta.get_saldo() for conta in self.contas)

    def remover_conta_por_titular(self, titular):
        conta = self.buscar_conta(titular)
        if conta:
            self.contas.remove(conta)
            return True
        return False


if __name__ == "__main__":
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

    print(f"Saldo total do banco: {banco.saldo_total()}")
