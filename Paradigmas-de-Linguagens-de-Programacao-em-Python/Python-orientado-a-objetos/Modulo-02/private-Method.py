class Circulo:
  def __init__(self,clientes,numero,saldo):
    self.clientes = clientes
    self.numero = numero
    self.saldo = saldo

  def __gerarsaldo(self):
    print(f"numero: {self.numero}\n saldo:{self.saldo}")
