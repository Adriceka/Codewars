def generate_shape(n):
    cuadrado = []
    for i in range(n):
        fila = "+" * n
        cuadrado.append(fila)
    return "\n".join(cuadrado)

if __name__ == '__main__':
    assert generate_shape(3) == '+++\n+++\n+++'
    assert generate_shape(8) == '++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++'