def is_happy(n):
    vistos = set()
    while n != 1 and n not in vistos:
        vistos.add(n)
        n = sum(int(d)**2 for d in str(n))
    return n == 1

if __name__ == '__main__':
        assert is_happy(19) == True
        assert is_happy(2) == False
        assert is_happy(7) == True
        assert is_happy(4) == False
        assert is_happy(1) == True
        assert is_happy(0) == False
        assert is_happy(100) == True
        assert is_happy(123456789) == False
