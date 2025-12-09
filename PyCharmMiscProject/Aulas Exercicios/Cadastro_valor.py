def cadastrar_valores():
    valores = {
        "valor 1": float(input("Digite o valor 1: ")),
        "valor 2": float(input("Digite o valor 2: ")),
    }
    soma = valores["valor 1"] + valores["valor 2"]
    return soma

resultado = cadastrar_valores()
print("A soma é:", resultado)