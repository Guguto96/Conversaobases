DIGITOS = "0123456789ABCDEF"


def decimal_para_base(numero, base):
    """Converte um número decimal inteiro para outra base."""
    if numero == 0:
        return "0"

    negativo = numero < 0
    numero = abs(numero)
    resultado = ""

    while numero > 0:
        resto = numero % base
        resultado = DIGITOS[resto] + resultado
        numero //= base

    if negativo:
        resultado = "-" + resultado

    return resultado


def base_para_decimal(numero, base):
    """Converte um número de uma base qualquer para decimal."""
    numero = numero.strip().upper()

    if not numero:
        raise ValueError("Digite um número.")

    negativo = numero.startswith("-")

    if negativo:
        numero = numero[1:]

    if not numero:
        raise ValueError("Número inválido.")

    resultado = 0

    for caractere in numero:
        if caractere not in DIGITOS[:base]:
            raise ValueError(
                f"O caractere '{caractere}' não é válido na base {base}."
            )

        valor = DIGITOS.index(caractere)
        resultado = resultado * base + valor

    return -resultado if negativo else resultado


def converter(numero, base_origem, base_destino):
    """Converte um número entre as bases 2, 8, 10 e 16."""
    bases_validas = (2, 8, 10, 16)

    if base_origem not in bases_validas:
        raise ValueError("Base de origem inválida.")

    if base_destino not in bases_validas:
        raise ValueError("Base de destino inválida.")

    valor_decimal = base_para_decimal(numero, base_origem)

    return decimal_para_base(valor_decimal, base_destino)
