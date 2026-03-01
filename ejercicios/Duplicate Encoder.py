def duplicate_encode(word):
    word = word.lower()
    resultado = ""
    for character in word:
        if word.count(character) > 1:
            resultado += ')'
        else:
            resultado += '('
    return resultado

if __name__ == '__main__':
        assert duplicate_encode("din") == "((("
        assert duplicate_encode("recede") == "()()()"
        assert duplicate_encode("Success") == ")())())"
        assert duplicate_encode("(( @") == "))(("