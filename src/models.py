import json

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
    
    def a_diccionario(self):
        usuario_dict = {"nombre": self.nombre, "correo": self.correo, "saldo": self.saldo}
        return usuario_dict
        
def guardar_usuarios(usuarios, archivo_nombre="usuarios.json"):
    lista_usuarios = [usuario.a_diccionario() for usuario in usuarios]
    with open(archivo_nombre, "w") as archivo:
        json.dump(lista_usuarios, archivo)

def cargar_usuarios(archivo_nombre="usuarios.json"):
    with open(archivo_nombre, "r") as archivo:
        lista_usuarios = json.load(archivo)

    usuarios = [Usuario(d["nombre"], d["correo"], d["saldo"]) for d in lista_usuarios]
    return usuarios
