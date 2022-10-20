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
    if a <= 0 or b <= 0 or c <= 0:
        return 'do not mean sides'
    else:
        if a + b <= c:
            return 'impossible'
        elif a == b and b == c:
            return 'equilateral'
        elif a == b or a == c or b == c:
            return 'isosceles'
        else:
            return 'various'


def task3(str):
    return '\n'.join(str.split(' '))


def kadane(arr, start, finish, n):
    Sum = 0
    maxSum = -999999999999
    i = None

    finish[0] = -1

    local_start = 0

    for i in range(n):
        Sum += arr[i]
        if Sum < 0:
            Sum = 0
            local_start = i + 1
        elif Sum > maxSum:
            maxSum = Sum
            start[0] = local_start
            finish[0] = i

    if finish[0] != -1:
        return maxSum

    maxSum = arr[0]
    start[0] = finish[0] = 0

    for i in range(1, n):
        if arr[i] > maxSum:
            maxSum = arr[i]
            start[0] = finish[0] = i
    return maxSum


def findMaxSum(arr):
    global ROW, COL
    ROW = len(arr)
    COL = len(arr[0])
    maxSum, finalLeft = -999999999999, None

    left, right, i = None, None, None

    temp = [None] * ROW
    Sum = 0
    start = [0]
    finish = [0]

    for left in range(COL):

        temp = [0] * ROW

        for right in range(left, COL):

            for i in range(ROW):
                temp[i] += arr[i][right]

            Sum = kadane(temp, start, finish, ROW)

            if Sum > maxSum:
                maxSum = Sum

    return maxSum




def open_file(string):
    with open(string) as f:
        symbols = f.read()

    items = symbols.split()
    res = [int(x) for x in items]
    return res


def main():
    print('~~~Task 1~~~')
    res_arr = open_file('test.txt')
    positive_number_amount, negative_number_amount, negative_number_average = task1(res_arr)
    print(f'Amount of positive: {positive_number_amount}')
    print(f'Amount of negative: {negative_number_amount}')
    print(f'The arithmetic mean of negative numbers: {negative_number_average}')
    print(res_arr)
    print('\n~~~Task 2~~~')
    print(task_2(6.5, 5.4, 5.4), '\n')
    print('~~~Task 3~~~')
    str = 'i love Ukraine'
    print(task3(str))
    print('~~~Task 4~~~')
    M = [[1, 2, -1, -4],
         [-8, -3, 4, 2],
         [3, 8, 10, 1],
         [-4, -1, 1, 7]]

    print("Max sum is:",findMaxSum(M))


if __name__ == '__main__':
    main()
