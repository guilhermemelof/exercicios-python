def resposta(valor, tipo):
    if tipo == "C":
        return float((9 * valor / 5) + 32)
    else:
        return float((valor - 32) * 5 / 9)
