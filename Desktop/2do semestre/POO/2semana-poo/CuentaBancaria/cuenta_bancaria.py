class CuentaBancaria:

    def __init__(self, titular, numero_cuenta, saldo=0):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Depósito exitoso de ${cantidad}. Saldo actual: ${self.saldo}")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Fondos insuficientes")
        else:
            self.saldo -= cantidad
            print(f"Retiro exitoso de ${cantidad}. Saldo actual: ${self.saldo}")
 
    def consultar_saldo(self):
        print(f"Titular: {self.titular} | Cuenta: {self.numero_cuenta} | Saldo: ${self.saldo}")

cuenta1 = CuentaBancaria("Dennis Leo Pacheco", "001-123456", 500)

cuenta2 = CuentaBancaria("Juan Pérez", "001-789012", 1000)
    
print("=== CUENTA 1 ===")
cuenta1.consultar_saldo() 
cuenta1.depositar(200)
cuenta1.retirar(100)
cuenta1.retirar(700)
cuenta1.consultar_saldo()

print("\n=== CUENTA 2 ===")
cuenta2.consultar_saldo()
cuenta2.depositar(500)
cuenta2.retirar(300)
cuenta2.consultar_saldo()