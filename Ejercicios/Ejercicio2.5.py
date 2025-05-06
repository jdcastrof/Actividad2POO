from enum import Enum

class TipoCuenta(Enum):
    AHORROS = "AHORROS"
    CORRIENTE = "CORRIENTE"

class CuentaBancaria:
    def __init__(self, nombresTitular, apellidosTitular, numeroCuenta, tipoCuenta):
        self.nombresTitular = nombresTitular
        self.apellidosTitular = apellidosTitular
        self.numeroCuenta = numeroCuenta
        self.tipoCuenta = tipoCuenta
        self.saldo = 0.0

    def imprimir(self):
        print(f"Nombres del titular = {self.nombresTitular}")
        print(f"Apellidos del titular = {self.apellidosTitular}")
        print(f"Número de cuenta = {self.numeroCuenta}")
        print(f"Tipo de cuenta = {self.tipoCuenta.value}")
        print(f"Saldo = ${self.saldo:,.2f}")

    def consultarSaldo(self):
        print(f"El saldo actual es = ${self.saldo:,.2f}")

    def consignar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Se ha consignado ${valor:,.2f} en la cuenta. El nuevo saldo es ${self.saldo:,.2f}")
            return True
        else:
            print("El valor a consignar debe ser mayor que cero.")
            return False

    def retirar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Se ha retirado ${valor:,.2f} en la cuenta. El nuevo saldo es ${self.saldo:,.2f}")
            return True
        else:
            print("El valor a retirar debe ser menor o igual al saldo actual y mayor que cero.")
            return False

if __name__ == "__main__":
    cuenta = CuentaBancaria("Pedro", "Pérez", 123456789, TipoCuenta.AHORROS)
    cuenta.imprimir()
    cuenta.consignar(200000)
    cuenta.consignar(300000)
    cuenta.retirar(400000)
  
