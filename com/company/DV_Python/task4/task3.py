import logging
import sys


logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)

file_handler = logging.FileHandler('logs.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)


logger.addHandler(file_handler)
logger.addHandler(stdout_handler)


class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def push(self, value):
        logger.info("Push value")
        self.stack.append(value)
        return self

    def pop(self):
        logger.info("Pop value")
        if self.stack:
            return self.stack.pop()
        else:
            return None

    def empty(self):
        logger.info("Empty function")
        return not self.stack

    def len(self):
        logger.info("Len of stack")
        return len(self.stack)

    def clear(self):
        logger.info("Clear stack")
        self.stack.clear()


def evaluate(formula: str) -> int:
    operators = Stack()
    numbers = Stack()
    i = 0

    while i < len(formula):
        char = formula[i]

        logger.info("Push operator to operators stack")
        if char == 'S' or char == 'D':
            operators.push(char)


        # push number to numbers stack
        elif char.isdigit():
            number_start = i
            while formula[i+1].isdigit():
                i += 1
            number = formula[number_start:i+1]
            numbers.push(int(number))

        # ("pop operator and numbers and perform calculations")
        elif char == ')':
            op = operators.pop()
            rhs = numbers.pop()
            lhs = numbers.pop()
            if op == 'S':
                numbers.push(lhs + rhs)
            elif op == 'D':
                numbers.push(int(lhs / rhs))

        i += 1

    result = numbers.pop()
    return result


help_msg = \
    """
    Available commands

    help        show this help message
    formula     enter formula manually
    test1       S(2,2)
                expected 4
    test2       D(4,2)
                expected 2
    test3       D(5,2)
                expected 2
    test4       D(8,S(2,1))
                expected 2
    test5       S(D(10,2),D(S(20,4),3))
                expected 13
    exit        exit
    """


def main():
    logger.info('Welcome! Type "help" for more information. Type "exit" to exit.')

    while True:
        command = input('> ')

        if command == 'help':
            logger.info(help_msg)

        elif command == 'exit':
            return

        elif not command:
            pass

        else:
            if command == 'formula':
                formula = input('formula> ')

            elif command == 'test1':
                formula = 'S(2,2)'

            elif command == 'test2':
                formula = 'D(4,2)'

            elif command == 'test3':
                formula = 'D(5,2)'

            elif command == 'test4':
                formula = "D(8,S(2,1))"

            elif command == 'test5':
                formula = "S(D(10,2),D(S(20,4),3))"

            else:
                logger.info(f'Unknown command: {command}')
                continue

            result = evaluate(formula)
            logger.info(result)


if __name__ == '__main__':
    main()
