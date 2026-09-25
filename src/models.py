class SaldoInsuficienteError(Exception):
    pass

class SaldoNegativoError(Exception):
    pass

class Usuario:
    def __init__(self, nombre, correo, saldo):
        self.nombre = nombre
        self.correo = correo
        self.saldo = saldo

    def depositar(self, monto):
        if monto < 0:
            raise SaldoNegativoError("No se puede tener saldo negativo")
        self.saldo = self.saldo + monto
    
    def retirar(self, monto):
        if monto > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente")
 
        self.saldo = self.saldo - monto
        return "Retiro exitoso"
        
