def rotate(data, n):
    if not data or n == 0:
        return data

    longitud = len(data)
    n = n % longitud  

    return data[-n:] + data[:-n]

if __name__ == '__main__':
        assert rotate([1, 2, 3, 4, 5], 1) == [5, 1, 2, 3, 4]
        assert rotate([1, 2, 3, 4, 5], -1) == [2, 3, 4, 5, 1]
        assert rotate([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
        assert rotate([1, 2, 3, 4, 5], -2) == [3, 4, 5, 1, 2]
        assert rotate([1, 2, 3, 4, 5], 3) == [3, 4, 5, 1, 2]
        assert rotate([1, 2, 3, 4, 5], -3) == [4, 5, 1, 2, 3]
        assert rotate([1, 2, 3, 4, 5], 4) == [2, 3, 4, 5, 1]
        assert rotate([1, 2, 3, 4, 5], -4) == [5, 1, 2, 3, 4]
        assert rotate([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]
        assert rotate([1, 2, 3, 4, 5], -5) == [1, 2, 3, 4, 5]
        assert rotate([1, 2, 3, 4, 5], 6) == [5, 1, 2, 3, 4]
        assert rotate([1, 2, 3, 4, 5], -6) == [2, 3, 4, 5, 1]
        assert rotate([True, True, False], 2) == [True, False, True]
        assert rotate([1, 2, 3, 4, 5], -12478) == [3 ,4 ,5 ,1 ,2]
        assert rotate([],976999) == []