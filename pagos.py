IMPUESTOS = {"CO": 0.19, "MX": 0.16, "CL": 0.19}


def calcular_descuento(monto, es_vip):
    if not es_vip:
        return monto
    if monto > 1000:
        return monto * 0.80  # 20% descuento
    return monto * 0.90  # 10% descuento


def procesar_pago_usuario(usuario, tarjeta, monto, pais, es_vip):
    if usuario is None:
        return False
    if not usuario["activo"]:
        print("Usuario inactivo")
        return False
    if tarjeta["saldo"] < monto:
        print("Saldo insuficiente")
        return False

    monto_final = calcular_descuento(monto, es_vip)
    monto_final += monto_final * IMPUESTOS.get(pais, 0)

    tarjeta["saldo"] -= monto_final
    return True
