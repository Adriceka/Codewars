def repeats(items):
    sum_singles = 0
    for item in items:
        if items.count(item) == 1:
            sum_singles += item
    return sum_singles

if __name__ == '__main__':
    assert repeats([4,5,7,5,4,8]) == 15
    assert repeats([9, 10, 19, 13, 19, 13]) == 19
    assert repeats([16, 0, 11, 4, 8, 16, 0, 11]) == 12
    assert repeats([5, 17, 18, 11, 13, 18, 11, 13]) == 22
    assert repeats([5, 10, 19, 13, 10, 13]) == 24