def cadastrar_pessoa():
    pessoa = {
        "nome": input("Digite seu nome: "),
        "idade": input("Digite sua idade: "),
        "cpf": input("Digite seu CPF: "),
        "estado_origem": input("Digite seu estado de origem: "),
        "cep": input("Digite seu CEP: "),
        "genero": input("Digite seu gênero: "),
        "telefone": input("Digite seu telefone: "),
        "fonte_pagadora": input("Digite sua fonte pagadora: ")
    }
    return pessoa


dados = cadastrar_pessoa()

print("\nPessoa cadastrada:")
for chave, valor in dados.items():
    print(f"{chave}: {valor}")


