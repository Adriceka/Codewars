def octopus(idea: str | None) -> str:
    if idea is None or idea.strip() == "":
        return ""

    resultado = []
    usados = {}       
    contador = 0   

    for c in idea:
        if contador == 8:
            usados.clear()
            contador = 0

        contador += 1

        clave = c.lower()

        if c.isdigit():
            if usados.get(clave, 0) < 2:
                usados[clave] = usados.get(clave, 0) + 1
                resultado.append(c)
            else:
                resultado.append('*')
        else:
            if clave not in usados:
                usados[clave] = 1
                resultado.append(c)
            else:
                resultado.append('*')

    return "".join(resultado)

if __name__ == '__main__':
        assert octopus("Can a can contain fish?") == "Can ****n co*tain fish?"
        assert octopus("8000 dollars went missing") == "800* dollars went mis**ng"
        assert octopus("Write 122 pages") == "Write 122 pages"
        assert octopus(None) == ""
        assert octopus("    ") == ""
        assert octopus("    1    1") == " ***1*** 1"
        assert octopus("a") == "a"
        assert octopus("Z") == "Z"
        assert octopus("5") == "5"
        assert octopus("?") == "?"
        assert octopus("aa") == "a*"
        assert octopus("AAA") == "A**"
        assert octopus("aaa") == "a**"
        assert octopus("111") == "11*"
        assert octopus("2222") == "22**"
        assert octopus("!!!") == "!**"
        assert octopus("a1a1") == "a1*1"
        assert octopus("Aa") == "A*"
        assert octopus("aA") == "a*"
        assert octopus("1a1a1a1a") == "1a1*****"
        assert octopus("abc123abc") == "abc123**c"
        assert octopus("Wait... What?") == "Wait.** What?"
        assert octopus("aaaaaaaaa") == "a*******a"
        assert octopus("111111111") == "11******1"
        assert octopus("abcdefgha") == "abcdefgha"
        assert octopus("abcdefghi") == "abcdefghi"
        assert octopus("abcdefghijkl") == "abcdefghijkl"
        assert octopus("Hello World!") == "Hel*o W*rld!"
        assert octopus("Can a can contain fish?") == "Can ****n co*tain fish?"
        assert octopus("8000 dollars went missing") == "800* dollars went mis**ng"
        assert octopus("Write 122 pages") == "Write 122 pages"
        assert octopus(None) == ""
        assert octopus("") == ""
        assert octopus("    ") == ""
        assert octopus("   a   ") == " **a***"