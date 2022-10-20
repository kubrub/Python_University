import datetime
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


class Queue:
    def __init__(self):
        self.queue = []

    def createFromList(self, newQueue):
        logger.info("create queue from list")
        self.queue = newQueue

    def __str__(self):
        return "<back> [" + ",".join(map(str, self.queue)) + "] <front>"

    def into(self, obj):
        logger.info("Insert value into queue")
        self.queue.insert(0, obj)
        return self

    def take(self):
        logger.info("Pop value from queue")
        if self.queue:
            return self.queue.pop()
        else:
            return None

    def __len__(self):
        logger.info("Len of queue")
        return len(self.queue)

    def front(self):
        logger.info("Front of queue")
        if self.queue:
            return self.queue[len(self.queue) - 1]
        else:
            return None

    def back(self):
        logger.info("Back of queue")
        if self.queue:
            return self.queue[0]
        else:
            return None

    def empty(self):
        logger.info("If queue is empty")
        return not self.queue

    def clear(self):
        logger.info("Clear queue")
        self.queue = []

    def find(self, key=lambda x: True):
        logger.info("Find x in queue")
        try:
            indexList = [i for i in range(len(self.queue)) if key(self.queue[i])]
            return indexList
        except:
            return []
        pass

    def remove(self, k):
        logger.info("Remove k from queue")
        if 0 <= k < len(self.queue):
            y = self.queue[k]
            del self.queue[k: k + 1]
            return y
        else:
            return None

    def all(self):
        return self.queue


class Border:
    def __init__(self, queue):
        self.general = queue

    def divideIntoQueues(self):
        logger.info("Divide into two queues. If total price of cars' goods is < 80000 car can go to green path")
        withDeclaration = Queue()
        greenPath = Queue()

        while len(self.general) > 0:
            car = self.general.take()
            if car['amount'] * car['price'] < 80000:
                greenPath.into(car)
            else:
                withDeclaration.into(car)

        return withDeclaration, greenPath

    def filterCars(self, queue, key, value):
        logger.info("Filter cars by specific key and thats key value")
        if key == 'from' or key == 'to':
            indexes = queue.find(lambda x: value in x[key])
        else:
            indexes = queue.find(lambda x: x[key] == value)
        return indexes


    def removeCarsFromRussia(self):
        logger.info("It is not safe to let cars from Russia go into country")
        indexes = self.filterCars(self.general, 'from', 'Russia')

        if len(indexes) != 0:
            deletedCount = 0
            for i in indexes:
                self.general.remove(i - deletedCount)
                deletedCount += 1
                logger.info(f'Car #{i} was removed from queue because it was from Russia')
        else:
            logger.info('There are not cars from Russia')


    def crossBorder(self, queue):
        logger.info("Move car through the border")
        goodsList = []
        carWithMaxTotalPrice = queue.front()
        maxTotalPrice = carWithMaxTotalPrice['price'] * carWithMaxTotalPrice['amount']

        while len(queue) > 0:
            car = queue.take()
            if car['withCarriageContract'] == True:
                model = car['model']
                number = car['number']
                goods = car['goods']
                amount = car['amount']
                price = car['price']
                isInGoodsList = False

                total_price = price * amount
                if total_price > maxTotalPrice:
                    carWithMaxTotalPrice = car
                    maxTotalPrice = total_price

                for st in goodsList:
                    if st['goods'] == goods:
                        isInGoodsList = True
                        st['amount'] += amount
                        st['total price'] += price * amount
                        break
                if not isInGoodsList:
                    goodsList.append({'goods': goods, 'price': price, 'amount': amount, 'total price': total_price})
                logger.info(f'\t{model} ({number}) crossed the border with country')
            else:
                model = car['model']
                number = car['number']
                logger.info(
                    f'\t{model} ({number}) was not allowed to crossed the border with country because it didn`t have carriage contract')

        return goodsList, carWithMaxTotalPrice, maxTotalPrice


def printStatistics(statistic):
    logger.info("Prity print statistic")
    logger.info(f'\t{statistic["goods"]}: Total Amount = {statistic["amount"]}, Total Price = {statistic["total price"]}')


def printCar(car):
    logger.info("Prity print car")
    logger.info(f'{car["model"]} ({car["number"]}):')
    logger.info(f'\t Company: {car["company"]}')
    logger.info(f'\t Date: {car["date"]}')
    logger.info(f'\t From: {car["from"][0]}, {car["from"][1]}')
    logger.info(f'\t To: {car["to"][0]}, {car["to"][1]}')
    logger.info(f'\t Goods: {car["goods"]}')
    logger.info(f'\t One good price: {car["price"]}')
    logger.info(f'\t Amount: {car["amount"]}')
    logger.info(f'\t With carriage contract: {"Yes" if car["withCarriageContract"] else "No"}')


def main():
    logger.info("Initialize general queue before dividing to 'green queue' and not 'green queue'")
    initialQueue = Queue()
    initialQueue.createFromList([
        {
            'model': 'Renault',
            'number': 'BC 5510 BT',
            'company': 'Asus',
            'date': datetime.datetime.strptime('01.10.2020', '%d.%m.%Y'),
            'from': ('Poland', 'Warsaw'),
            'to': ('Ukraine', 'Lviv'),
            'goods': 'laptop',
            'price': 30000,
            'amount': 10,
            'withCarriageContract': True
        },
        {
            'model': 'Audi',
            'number': 'н456cc',
            'company': 'LG',
            'date': datetime.datetime.strptime('04.10.2020', '%d.%m.%Y'),
            'from': ('Russia', 'Saint Petersburg'),
            'to': ('Ukraine', 'Harkiv'),
            'goods': 'microwave',
            'price': 5000,
            'amount': 5,
            'withCarriageContract': True
        },
        {
            'model': 'Volvo',
            'number': 'WOB ZK 295',
            'company': 'Svitoch',
            'date': datetime.datetime.strptime('05.10.2020', '%d.%m.%Y'),
            'from': ('German', 'Berlin'),
            'to': ('Ukraine', 'Odesa'),
            'goods': 'sweets',
            'price': 500,
            'amount': 20,
            'withCarriageContract': False
        },
        {
            'model': 'Nissan',
            'number': 'A24681R',
            'company': 'Kochut',
            'date': datetime.datetime.strptime('07.10.2020', '%d.%m.%Y'),
            'from': ('Austria', 'Vienna'),
            'to': ('Ukraine', 'Cherkasy'),
            'goods': 'jewelry',
            'price': 15000,
            'amount': 300,
            'withCarriageContract': True
        },
        {
            'model': 'BMW',
            'number': 'н123ex',
            'company': 'Roshen',
            'date': datetime.datetime.strptime('04.10.2020', '%d.%m.%Y'),
            'from': ('Russia', 'Moscow'),
            'to': ('Ukraine', 'Kyiv'),
            'goods': 'sweets',
            'price': 400,
            'amount': 25,
            'withCarriageContract': True
        },
        {
            'model': 'Renault',
            'number': 'KR 7854',
            'company': 'company4',
            'date': datetime.datetime.strptime('02.10.2020', '%d.%m.%Y'),
            'from': ('Poland', 'Wroclaw'),
            'to': ('Ukraine', 'Odesa'),
            'goods': 'laptop',
            'price': 25000,
            'amount': 15,
            'withCarriageContract': False
        },
        {
            'model': 'Volvo',
            'number': 'WJG 824',
            'company': 'Lenovo',
            'date': datetime.datetime.strptime('07.10.2020', '%d.%m.%Y'),
            'from': ('Sweden', 'Malmo'),
            'to': ('Ukraine', 'Kyiv'),
            'goods': 'laptop',
            'price': 28000,
            'amount': 13,
            'withCarriageContract': True
        },
        {
            'model': 'Ford',
            'number': 'AI 1562 EE',
            'company': 'Cube',
            'date': datetime.datetime.strptime('03.10.2020', '%d.%m.%Y'),
            'from': ('Hungary', 'Budapest'),
            'to': ('Ukraine', 'Cherkasy'),
            'goods': 'bicycle',
            'price': 10000,
            'amount': 10,
            'withCarriageContract': True
        },
        {
            'model': 'Ford',
            'number': 'AC 3333 BB',
            'company': 'Roshen',
            'date': datetime.datetime.strptime('04.10.2020', '%d.%m.%Y'),
            'from': ('Czech Republic', 'Brno'),
            'to': ('Ukraine', 'Kyiv'),
            'goods': 'sweets',
            'price': 550,
            'amount': 18,
            'withCarriageContract': False
        },
        {
            'model': 'Audi',
            'number': 'AA 7777 AA',
            'company': 'Kochut',
            'date': datetime.datetime.strptime('06.10.2020', '%d.%m.%Y'),
            'from': ('Romania', 'Bucharest'),
            'to': ('Ukraine', 'Lviv'),
            'goods': 'jewelry',
            'price': 25000,
            'amount': 170,
            'withCarriageContract': True
        }
    ])

    border = Border(initialQueue)
    border.removeCarsFromRussia()

    indexesInQueue = border.filterCars(initialQueue, 'goods', 'sweets')
    logger.info(f'\nIndexes of cars with sweets in initial queue: {indexesInQueue}')

    indexesInQueue = border.filterCars(initialQueue, 'to', 'Lviv')
    logger.info(f'Indexes of cars which go to Lviv in initial queue: {indexesInQueue}')

    withDeclaration, greenPath = border.divideIntoQueues()

    logger.info('\nCars entered the country from queue with declaration:')
    withDeclarationStatistics, carWithMaxTotalPrice, maxTotalPrice = border.crossBorder(withDeclaration)
    logger.info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for st in withDeclarationStatistics:
        printStatistics(st)
    logger.info(f'\nCar with max total price in queue with declaration: {maxTotalPrice}')
    printCar(carWithMaxTotalPrice)

    logger.info('\nCars entered the country from green path:')
    greenPathStatistics, carWithMaxTotalPrice, maxTotalPrice = border.crossBorder(greenPath)
    logger.info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for st in greenPathStatistics:
        printStatistics(st)
    logger.info(f'\nCar with max total price in green path: {maxTotalPrice}')
    printCar(carWithMaxTotalPrice)


if __name__ == '__main__':
    main()
