from collections import Counter

def comp(number_list_a, number_list_b):
    if number_list_a is None or number_list_b is None:
        return False

    squared_a = [x ** 2 for x in number_list_a]
    return Counter(squared_a) == Counter(number_list_b)

if __name__ == '__main__':
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    assert comp(a1, a2) == True
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    assert comp(a1, a2) == False
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
    assert comp(a1, a2) == False