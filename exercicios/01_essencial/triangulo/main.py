def resposta(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "não forma triângulo"
    if a == b == c:
        return "equilátero"
    if a == b or b == c or a == c:
        return "isósceles"
    return "escaleno"
