def resposta(peso):
    if peso > 50:
        excesso = peso - 50
        multa = excesso * 4
        return (excesso, multa)
    return (0, 0)
