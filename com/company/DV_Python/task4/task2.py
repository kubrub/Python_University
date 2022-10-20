class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def push(self, value):
        self.stack.append(value)
        return self

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None

    def empty(self):
        return not self.stack

    def len(self):
        return len(self.stack)

    def clear(self):
        self.stack.clear()


left_parentheses = {'(', '[', '{'}
right_parentheses = {')', ']', '}'}
match_parentheses = {')': '(', ']': '[', '}': '{'}
operands = {'x', 'y', 'z'}
operators = {'+', '-'}


def check_formula(formula: str) -> bool:
    stack = Stack()

    for char in formula:
        if char in left_parentheses:
            stack.push(char)
        elif char in operands:
            # mark operands as F
            stack.push('F')
        elif char in operators:
            stack.push(char)
        elif char in right_parentheses:
            while True:
                # value on top of the stack before closing parenthesis
                # must always be F (i.e. operand)
                rhs = stack.pop()
                if rhs != 'F':
                    return False
                # next value must be either operator or matching parenthesis
                # (in which case last operand should be pushed back into
                # the stack and loop stopped)
                op = stack.pop()
                if op == match_parentheses[char]:
                    stack.push('F')
                    break
                elif op not in operators:
                    return False
                # if last extracted value is an operator than there must
                # be other operand
                lhs = stack.pop()
                if lhs != 'F':
                    return False
                # if all previous steps were successful push 'computation'
                # result (which is also an operand) into the stack
                stack.push('F')

    # perform simillar steps as above until stack is not empty
    # that is needed to check what is left after processing all parentheses
    while not stack.empty():
        rhs = stack.pop()
        if rhs != 'F':
            return False
        if stack.empty():
            break
        op = stack.pop()
        if op not in operators:
            return False
        lhs = stack.pop()
        if lhs != 'F':
            return False
        stack.push('F')

    return True


help_msg = \
    """
    Available commands

    help        show this help message
    formula     enter formula manually
    test1       x + ( y - z - [ x + x ] + { [ z - z - y ] + ( y ) } ) - z
                expected True
    test2       {(x)}
                expected True
    test3       x + y + z
                expected True
    test4       x + (x - (y + z)
                expected False
    test5       x +
                expected False
    test6       x + [y + z}
                expected False
    exit        exit
    """


def main():
    print('Welcome! Type "help" for more information. '
          'Type "exit" to exit.')

    while True:
        command = input('> ')

        if command == 'help':
            print(help_msg)

        elif command == 'exit':
            return

        elif not command:
            pass

        else:
            if command == 'formula':
                formula = input('formula> ')

            elif command == 'test1':
                formula = \
                    'x + ( y - z - [ x + x ] + { [ z - z - y ] + ( y ) } ) - z'

            elif command == 'test2':
                formula = '{(x)}'

            elif command == 'test3':
                formula = 'x + y + z'

            elif command == 'test4':
                formula = 'x + (x - (y + z)'

            elif command == 'test5':
                formula = 'x +'

            elif command == 'test6':
                formula = 'x + [y + z}'

            else:
                print(f'Unknown command: {command}')
                continue

            result = check_formula(formula)
            print(result)


if __name__ == '__main__':
    main()
