"""
Testing Triangle Classification
@uthor : Adithya Varma Created on: 02/03/20
"""

def classify_triangle(a, b, c):
    """ Function that determines the type of triangle """
    if  type(a) != int or type(b) != int or type(c) != int or a + b <= c or b + c <= a or c + a <= b:
        return 'It is an Invalid Triangle'
    else:
        if a == b == c:
            return 'It is an Equilateral Triangle'
        elif a == b or b == c or a == c:
            return 'It is an Isoceles Triangle'
        elif a*a + b*b == c*c or b*b + c*c == a*a or c*c + a*a == b*b:
            return 'It is a Right Triangle'
        else:
            return 'It is a Scalene Triangle'
    
def main():
    """ Function that gets the input from the user """
    try:
        print('Enter the sides of the triangle')
        x = input('a = ')
        y = input('b = ')
        z = input('c = ')
    except ValueError:
        'Enter a valid integer'
    print(classify_triangle(x, y, z))
    
main()