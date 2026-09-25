from src.validaciones import validar_usuario

def test_nombre_vacio():
    es_valido, mensaje = validar_usuario("", "correo@ejemplo.com", 100)
    assert es_valido == False

def test_correo_invalido():
    es_valido, mensaje = validar_usuario("nombre", "correoinvalido", 100)
    assert es_valido == False

def test_monto_negativo():
    es_valido, mensaje = validar_usuario("nombre", "correo@ejemplo", -1)
    assert es_valido == False

def test_usuario_valido():
    es_valido, mensaje = validar_usuario("Neza", "neza@correo.com", 100000000)
    assert es_valido == True