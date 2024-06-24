import sys

def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python palindromo.py <palabra>")
        sys.exit(1)
    
    palabra = sys.argv[1]
    resultado = es_palindromo(palabra)

    if resultado:
        print(f"{palabra} es un palíndromo.")
    else:
        print(f"{palabra} no es un palíndromo.")
