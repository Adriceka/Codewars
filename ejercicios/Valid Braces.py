def valid_braces(string):
    simbolos_abiertos = []
    pares = {')': '(', ']': '[', '}': '{'}

    for caracter in string:
        if caracter in '([{':
            simbolos_abiertos.append(caracter)
        else:
            if not simbolos_abiertos or simbolos_abiertos[-1] != pares[caracter]:
                return False
            simbolos_abiertos.pop()

    return not simbolos_abiertos

if __name__ == '__main__':
    assert valid_braces("(){}[]") == True
    assert valid_braces("([{}])") == True
    assert valid_braces("(}") == False
    assert valid_braces("[(])") == False
    assert valid_braces("[({})](]") == False