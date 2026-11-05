import pytest
from descuentos import calcular_precio_final


def test_cliente_vip_con_cupon():
    # Arrange & Act
    resultado = calcular_precio_final(100.0, es_vip=True, cupon="DESCUENTO10")
    # Assert
    assert resultado == 70.0


def test_precio_invalido_lanza_excepcion():
    with pytest.raises(ValueError):
        calcular_precio_final(-10, es_vip=False)


def test_cupon_superpromo_aplica_50_por_ciento():
    resultado = calcular_precio_final(100.0, es_vip=False, cupon="SUPERPROMO")
    assert resultado == pytest.approx(50.0)


def test_cupon_oro_aplica_30_por_ciento():
    resultado = calcular_precio_final(100.0, es_vip=False, cupon="ORO")
    assert resultado == pytest.approx(70.0)


def test_cliente_normal_sin_cupon_no_tiene_descuento():
    resultado = calcular_precio_final(100.0, es_vip=False)
    assert resultado == pytest.approx(100.0)