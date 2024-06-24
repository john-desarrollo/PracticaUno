def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]

if __name__ == "__main__":
    palabra = input("Ingresa una palabra: ")
    if es_palindromo(palabra):
        print(f'"{palabra}" es un palíndromo.')
    else:
        print(f'"{palabra}" no es un palíndromo.')