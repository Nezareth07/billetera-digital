from database import obtener_sesion
from db_models import UsuarioDB
from models import Usuario

def guardar_usuario_db(usuario):
    sesion = obtener_sesion()
    nuevo = UsuarioDB(nombre=usuario.nombre, correo=usuario.correo, saldo=usuario.saldo)
    sesion.add(nuevo)
    sesion.commit()
    sesion.close()

def cargar_usuarios_db():
    sesion = obtener_sesion()
    filas = sesion.query(UsuarioDB).all()
    usuarios = [Usuario(f.nombre, f.correo, f.saldo) for f in filas]
    sesion.close()
    return usuarios