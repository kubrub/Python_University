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
        logger.info("push element")
        self.stack.append(value)
        return self

    def pop(self):
        logger.info("pop element")
        if self.stack:
            return self.stack.pop()
        else:
            return None

    def empty(self):
        logger.info("check if stack is empty")
        return not self.stack

    def len(self):
        logger.info("len of stack")
        return len(self.stack)

    def clear(self):
        logger.info("clear stack")
        self.stack.clear()


def get_parentheses_pairs(formula: str) -> list:
    logger.info("get parentheses of pairs")
    stack = Stack()
    pairs = []
    for i in range(len(formula)):
        if formula[i] == '(':
            stack.push(i)
        elif formula[i] == ')':
            j = stack.pop()
            pairs.append((j, i))
    return pairs


def print_pairs(pairs: list):
    for pair in pairs:
        logger.info(f"{pair[0]} - {pair[1]}")


help_msg = \
    """
    Available commands

    help        show this help message
    formula     enter formula manually
    test1       (2 + 2)
                0.....6
    test2       (2 * (2 + 2))
                0....5....11.12
    test3       3 * ( (3 + 5) + (2 + 7) + 4 * (2 * (3 - 5) + 5 * (5 + 7) ) )
                ....4.6....12..16....22......30...35....41......49....55.57.59
    test4       2 + 2
                .....
    exit        exit
    """


def main():
    logger.info('Welcome! Type "help" for more information. '
          'Type "exit" to exit.')

    while True:
        command = input('> ')

        if command == 'help':
            logger.info(help_msg)

        elif command == 'exit':
            logger.info("exit")
            return

        elif not command:
            pass

        else:
            if command == 'formula':
                formula = input('formula> ')

            elif command == 'test1':
                formula = "(2 + 2)"

            elif command == 'test2':
                formula = '(2 * (2 + 2))'

            elif command == 'test3':
                formula = ("3 * ( (3 + 5) + (2 + 7) + "
                           "4 * (2 * (3 - 5) + 5 * (5 + 7) ) )")

            elif command == 'test4':
                formula = '2 + 2'

            else:
                logger.info(f'Unknown command: {command}')
                continue

            pairs = get_parentheses_pairs(formula)
            if pairs:
                logger.info("Print pairs - ", print_pairs(pairs))
                logger.info("Sorted by opening parenthesis: ", print_pairs(sorted(pairs, key=lambda x: x[0])))
                logger.info("Sorted by closing parenthesis: ", print_pairs(sorted(pairs, key=lambda x: x[1])))
            else:
                logger.info("No parentheses")


if __name__ == '__main__':
    main()
