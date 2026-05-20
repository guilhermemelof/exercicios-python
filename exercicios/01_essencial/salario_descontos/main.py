def resposta(valor, horas):
    bruto = valor * horas
    ir = bruto * 0.11
    inss = bruto * 0.08
    sindicato = bruto * 0.05
    liquido = bruto - ir - inss - sindicato
    return (int(bruto), int(ir), int(inss), int(sindicato), int(liquido))
