def es_palindromo(palabra):
    palabra = palabra.lower()  # Convertimos la palabra a minúsculas para evitar problemas de mayúsculas
    return palabra == palabra[::-1]  # Comparamos la palabra con su reverso

palabra_usuario = input("Ingrese una palabra: ")

if es_palindromo(palabra_usuario):
    print("La palabra es un palíndromo!")
else:
    print("La palabra no es un palíndromo.")
