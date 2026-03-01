def max_pizza(cuts):
    if cuts < 0:
        return -1
    return cuts * (cuts + 1) // 2 + 1

if __name__ == '__main__':
        assert max_pizza(-2) == -1
        assert max_pizza(0) == 1
        assert max_pizza(3) == 7
        assert max_pizza(4) == 11
        assert max_pizza(5) == 16
        assert max_pizza(6) == 22