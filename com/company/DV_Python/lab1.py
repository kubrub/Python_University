def task1(arr):
    positive_amount = 0
    negative_amount = 0
    negative_average = 0

    for i in range(len(arr)):
        if arr[i] > 0:
            positive_amount += 1
        elif arr[i] < 0:
            negative_amount += 1
            negative_average += arr[i]

    negative_average = negative_average / negative_amount if negative_amount != 0 else 0

    return positive_amount, negative_amount, negative_average


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


def open_file(string):
    with open(string) as f:
        symbols = f.read()

    items = symbols.split()
    res = [int(x) for x in items]
    return res


print('~~~Task 1~~~')
res_arr = open_file('test.txt')
positive_number_amount, negative_number_amount, negative_number_average = task1(res_arr)
print(f'Amount of positive: {positive_number_amount}')
print(f'Amount of negative: {negative_number_amount}')
print(f'The arithmetic mean of negative numbers: {negative_number_average}')
print('\n~~~Task 2~~~')
print(task_2(6, 5, 4), '\n')
print('~~~Task 3~~~')
str = 'i love Ukraine'
print(task3(str))