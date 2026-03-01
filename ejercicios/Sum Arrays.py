def sum_array(numeros):
    if not numeros:
        return 0
    return sum(numeros)

if __name__ == '__main__':
        assert sum_array([]) == 0
        assert sum_array([1, 2, 3]) == 6
        assert sum_array([1.1, 2.2, 3.3]) == 6.6
        assert sum_array([4, 5, 6]) == 15
        assert sum_array(range(101)) == 5050