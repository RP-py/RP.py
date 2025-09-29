def palindromo(texto):
    texto_limpio = texto.replace(" ", "").lower()
    return texto_limpio == texto_limpio[::-1]

frase = input("Ingresa una palabra o frase: ")
if palindromo(frase):
    print("es palindormo")
else:
    print("no es palindromo")

def anagramas(p1, p2):
    p1 = p1.replace(" ", "").lower()
    p2 = p2.replace(" ", "").lower()

    if len(p1) != len(p2):
        return False

    for letra in p1:
        if p1.count(letra) != p2.count(letra):
            return False

    return True
palabra1 = input("primera palabra: ")
palabra2 = input("segunda palabra: ")

if son_anagramas(palabra1, palabra2):
    print("son anagramas.")
else:
    print("no son anagramas.")
