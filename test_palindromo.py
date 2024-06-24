import pytest
from palindromo import es_palindromo

def test_palindromo():
    assert es_palindromo("radar") == True
    assert es_palindromo("python") == False
    assert es_palindromo("Ana") == True
    assert es_palindromo("Nivel") == True
    assert es_palindromo("Jenkins") == False

if __name__ == "__main__":
    pytest.main()