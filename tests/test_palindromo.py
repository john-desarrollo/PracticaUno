from palindromo import es_palindromo

def test_palindromo():
    assert es_palindromo("radar") == True
    assert es_palindromo("hello") == False
    assert es_palindromo("Ana") == True
