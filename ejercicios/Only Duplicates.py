def only_duplicates(st):
    contador = {}
    for letra_duplicada in st:  #"st" seria el nombre "string" abreviado
        if letra_duplicada in contador:
            contador[letra_duplicada] += 1
        else:
            contador[letra_duplicada] = 1

    resultado = ""
    for letra_duplicada in st:  
        if contador[letra_duplicada] > 1:
            resultado += letra_duplicada

    return resultado

if __name__ == '__main__':
        assert only_duplicates('abccdefee') == 'cceee'
        assert only_duplicates('hello') == 'll'
        assert only_duplicates('colloquial') == 'ollol'
        assert only_duplicates('foundersandcoders') == 'ondersndoders'
        assert only_duplicates('12314256aaeff') == '1212aaff'