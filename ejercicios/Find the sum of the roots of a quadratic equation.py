import math

def roots(a,b,c):

    discriminant = b ** 2 - 4 * a * c
    if discriminant >= 0:
        positive = (-b + math.sqrt(discriminant)) / (2 * a)
        negative = (-b - math.sqrt(discriminant)) / (2 * a)
        return round ((positive + negative), 2)
    else:
        return None
    
if __name__ == '__main__':
        assert roots(1,-35,-23) == 35
        assert roots(6,0,-24) == 0
        assert roots(-5,21,0) == 4.2
        assert roots(6,4,8) == None
        assert roots(1,5,-24) == -5
        assert roots(3,11,6) == -3.67
        assert roots(2,2,9) == None
        assert roots(1,-5/3,-26) == 1.67
        assert roots(1,6,10) == None
        assert roots(7,-2,-5) == 0.29
        assert roots(1,8,20) == None
        assert roots(2,3,-2) == -1.5
        assert roots(1,4,12) == None
        assert roots(3,-2,-5) == 0.67
        assert roots(3,4,9) == None
        assert roots(5,4,0) == -0.8
        assert roots(4,-5,0) == 1.25
        assert roots(1,4,9) == None
        assert roots(1,0,-49) == 0
        assert roots(2,8,8) == -4
        assert roots(1,0,-0.16) == 0
        assert roots(1,6,12) == None
        assert roots(1,0,-9) == 0
        assert roots(-3,0,12) == 0
        assert roots(1,3,9) == None
        assert roots(3,7,0) == -2.33
        assert roots(5,3,6) == None
        assert roots(1,4,4) == -4
        assert roots(-1,0,5.29) == 0
        assert roots(1,12,36) == -12
        assert roots(1,0,-0.09) == 0
        assert roots(2,5,11) == None
        assert roots(3,0,-15) == 0
        assert roots(1,-3,0) == 3
        assert roots(1,8,16) == -8
        assert roots(2,6,9) == None
        assert roots(-1,36,0) == 36
        assert roots(5,-8,0) == 1.6
        assert roots(1,5,12) == None
        assert roots(-14,0,0) == 0
        assert roots(1,7,20) == None
        assert roots(1,-6,0) == 6
        assert roots(1,-11,30) == 11
        assert roots(1,3,12) == None
        assert roots(1,6,9) == -6
        assert roots(8, 47, 41) == -5.88