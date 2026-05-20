def resposta(cigarros, anos):
    minutos_perdidos = cigarros * anos * 365 * 10
    return int(minutos_perdidos / 1440)
