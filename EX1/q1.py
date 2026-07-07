import math

x1, y1, x2, y2, x3, y3 = eval(input('Enter three points: '))

a = math.sqrt((x2-x3)**2 + (y2-y3)**2)
b = math.sqrt((x1-x3)**2 + (y1-y3)**2)
c = math.sqrt((x1-x2)**2 + (y1-y2)**2)

if a+b<=c or b+c<=a or a+c<=b:
    print('The three points do not form a triangle.')
else:
    A = math.degrees(math.acos((a*a - b*b - c*c)/ (-2*b*c)))
    B = math.degrees(math.acos((b*b - a*a - c*c)/ (-2*a*c)))
    C = math.degrees(math.acos((c*c - b*b - a*a)/ (-2*a*b)))

    print(f'The three angles, A, B, C are {A:.2f} {B:.2f} {C:.2f}')
