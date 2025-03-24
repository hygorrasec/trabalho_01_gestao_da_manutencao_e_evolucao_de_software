import unittest
from banco import ContaBancaria, Banco


class TestBanco(unittest.TestCase):
    def setUp(self):
        self.banco = Banco()
        self.conta1 = ContaBancaria("Ana", 1000)
        self.conta2 = ContaBancaria("Bruno", 500)
        self.banco.adicionar_conta(self.conta1)
        self.banco.adicionar_conta(self.conta2)

    def test_deposito_valido(self):
        self.assertTrue(self.conta1.depositar(500))
        self.assertEqual(self.conta1.get_saldo(), 1500)

    def test_saque_invalido(self):
        self.assertFalse(self.conta2.sacar(1000))

    def test_transferencia_valida(self):
        self.assertTrue(self.conta1.transferir_para(self.conta2, 300))
        self.assertEqual(self.conta1.get_saldo(), 700)
        self.assertEqual(self.conta2.get_saldo(), 800)

    def test_busca_case_insensitive(self):
        conta = self.banco.buscar_conta("ana")
        self.assertIsNotNone(conta)

    def test_remocao_de_conta(self):
        self.assertTrue(self.banco.remover_conta_por_titular("Bruno"))
        self.assertIsNone(self.banco.buscar_conta("Bruno"))


if __name__ == "__main__":
    unittest.main()
