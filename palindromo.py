def es_palindromo(palabra):
    palabra = palabra.lower()  # Convertir a minúsculas para comparación sin distinción de mayúsculas

    # Comparar la palabra con su reverso
    if palabra == palabra[::-1]:
        return True
    else:
        return False

if __name__ == "__main__":
    palabra = input("Ingresa una palabra para verificar si es un palíndromo: ")
    if es_palindromo(palabra):
        print(f"{palabra} es un palíndromo.")
    else:
        print(f"{palabra} no es un palíndromo.")