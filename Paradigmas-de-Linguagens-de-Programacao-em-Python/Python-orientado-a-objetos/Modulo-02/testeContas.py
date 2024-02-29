from Conta import Conta
cliente1 = Conta(1, 123, 'João', 0)
cliente2 = Conta(3, 456, 'Maria', 0)
conta1 = Conta([cliente1, cliente2], 1,0)
conta1.gerar_extrato()
conta1.depositar(1500)
conta1.sacar(500)
conta1.gerar_extrato()
