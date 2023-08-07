class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

propietarios = ["Juancho", "sofia"]
cuenta1 = CuentaBancaria("49852741", propietarios, 5000.0)

print(f"Número de cuenta: {cuenta1.numero_cuenta}")
print(f"Propietarios: {', '.join(cuenta1.propietarios)}")
print(f"Balance: {cuenta1.balance}")