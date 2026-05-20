def resposta(preco, percentual):
    desconto = preco * (percentual / 100)
    preco_final = preco - desconto
    return (int(desconto) if desconto == int(desconto) else desconto,
            int(preco_final) if preco_final == int(preco_final) else preco_final)
