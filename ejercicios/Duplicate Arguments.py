def solution(*valores):
    vistos = set()
    for valor in valores:
        if valor in vistos:
            return True
        vistos.add(valor)
    return False

if __name__ == '__main__':
        assert solution(1, 2, 3, 1, 2) == True
        assert solution() == False
        assert solution(1, 1) == True
        assert solution(1, 0) == False
        assert solution('a', 'b') == False
        assert solution('a', 'b', 'a') == True
        assert solution(1, 2, 42, 3, 4, 5, 42) == True
        assert solution('a', 'b', 'c', 'd') == False
        assert solution('a', 'b', 'c', 'd') == False
        assert solution('a', 'b', 'c', 'c') == True
        assert solution('a', 'b', 'c', 'd', 'e', 'f', 'f', 'b') == True