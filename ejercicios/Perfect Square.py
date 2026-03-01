def perfect_square(square):
    for c in square:
        if c != '.' and c != '\n':
            return False

    filas = square.split('\n')
    altura = len(filas)
    if altura == 0:
        return False

    ancho = len(filas[0])
    if ancho != altura:
        return False

    for fila in filas:
        if len(fila) != ancho:
            return False

    return True

if __name__ == '__main__':
        assert perfect_square('') == False
        assert perfect_square('..') == False
        assert perfect_square('...\n...') == False
        assert perfect_square('...\n...') == False
        assert perfect_square('....\n....\n....\n....') == True
        assert perfect_square('.....\n.....\n.....\n.....\n.....') == True
        assert perfect_square('....\n....\n....\n...') == False
        assert perfect_square('....\n....\n....\n.....') == False
        assert perfect_square('....\n....\n...x\n....') == False