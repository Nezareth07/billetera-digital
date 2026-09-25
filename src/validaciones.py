def validar_usuario(nombre, correo, monto):
    if nombre == "":
        return False, "Nombre vacío"
        
    if "@" not in correo:
        return False, "Ingresa un correo valido"
    
    if monto < 0:
        return False, "El monto no puede ser menor que cero"
    
    return True, "Usuario creado correctamente"