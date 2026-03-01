def dont_give_me_five(start, end):
    contador = 0
    
    for n in range(start, end + 1):
        if '5' not in str(n):
            contador += 1
            
    return contador

if __name__ == '__main__':
        assert dont_give_me_five(1, 9) == 8
        assert dont_give_me_five(4, 17) == 12
        assert dont_give_me_five(1, 100) == 90
        assert dont_give_me_five(1, 1000) == 900
        assert dont_give_me_five(1, 10000) == 9000
        assert dont_give_me_five(1, 100000) == 90000
        assert dont_give_me_five(1, 1000000) == 900000