LISTA_ALFABETO = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def criptografar(texto, chave):
    texto_criptografado = ''
    for letra in texto:
        letra_lower = letra.lower()
        if letra_lower in LISTA_ALFABETO:
            novo_index = (LISTA_ALFABETO.index(letra_lower) + chave) % 26
            nova_letra = LISTA_ALFABETO[novo_index]
            if letra.isupper():
                nova_letra = nova_letra.upper()
            texto_criptografado += nova_letra
        else:
            texto_criptografado += letra
    return texto_criptografado

def descriptografar(texto_criptografado, chave):
    texto_descrip = ''
    for letra in texto_criptografado:
        letra_lower = letra.lower()
        if letra_lower in LISTA_ALFABETO:
            novo_index = (LISTA_ALFABETO.index(letra_lower) - chave) % 26
            nova_letra = LISTA_ALFABETO[novo_index]
            if letra.isupper():
                nova_letra = nova_letra.upper()
            texto_descrip += nova_letra
        else:
            texto_descrip += letra
    return texto_descrip


texto_cifrado = criptografar("trilha python?", 5)
print(texto_cifrado)

texto_decifrado = descriptografar(texto_cifrado, 5)
print(texto_decifrado)