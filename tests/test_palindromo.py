import sys
import os

# Añadir el directorio raíz del proyecto al PATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from palindromo import es_palindromo

def test_palindromo():
    assert es_palindromo("radar") == True
    assert es_palindromo("hello") == False
    assert es_palindromo("Ana") == True