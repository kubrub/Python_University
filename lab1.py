def task_2(x, y, z):
    a, b, c = sorted([x, y, z])
    if a < 0 or b < 0 or c < 0:
        return False
    else:
        if a + b <= c:
            return 'impossible'
        elif a == b and b == c:
            return 'equilateral'
        elif a == b or a == c or b == c:
            return 'isosceles'
        elif c ** 2 == (a ** 2) + (b ** 2):
            return 'rectangular'
        elif ((a ** 2) + (b ** 2) - (c ** 2)) / (2 * a * b) > 0:
            return 'acute'
        else:
            return 'obtuse'


def task3(str):
    return '\n'.join(str.split(' '))

print(task_2(6, 5, 4), '\n')
str = 'i love Ukraine and u'
print(task3(str))