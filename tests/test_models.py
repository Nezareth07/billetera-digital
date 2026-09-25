import pytest
from src.models import Usuario, SaldoNegativoError, SaldoInsuficienteError

def test_deposito_valido():
    usuario = Usuario("Test", "test@correo.com", 500)
    usuario.depositar(200)
    assert usuario.saldo == 700

def test_retiro_valido():
    usuario = Usuario("Test", "test@correo.com", 500)
    usuario.retirar(500)
    assert usuario.saldo == 0

def test_deposito_invalido():
    usuario = Usuario("Test", "test@correo.com", 500)
    with pytest.raises(SaldoNegativoError):
        usuario.depositar(-1)

def test_retiro_invalido():
    usuario = Usuario("Test", "test@correo.com", 500)
    with pytest.raises(SaldoInsuficienteError):
        usuario.retirar(600)

