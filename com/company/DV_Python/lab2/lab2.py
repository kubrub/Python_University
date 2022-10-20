import csv
import datetime

properties = {
    'city': 'City',
    'country': 'Country',
    'date': 'Date',
    'temperature': 'Temperature',
    'conditions': 'Conditions',
}

propertiesList = list(properties.values())


def getData(fileName):
    data = []
    with open(fileName, newline='') as csvfile:
        weather_reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in weather_reader:
            newRow = row
            newRow['Date'] = datetime.datetime.strptime(row['Date'], '%d/%m/%Y %H:%M%f')
            newRow['Temperature'] = float(row['Temperature'])
            newRow['Conditions'] = row['Conditions']
            data.append(row)
    return data


def getByCityAndDate(data, city=None, date=None):
    result = []
    if city is not None and date is not None:
        for record in data:
            if record['City'] == city and record['Date'] == date:
                result.append(record)
    elif city is not None and date is None:
        for record in data:
            if record['City'] == city:
                result.append(record)
    elif city is None and date is not None:
        for record in data:
            if record['Date'] == date:
                result.append(record)
    else:
        return data
    return result


def getByCityAndDateRange(data, city=None, dateRange=None):
    result = []
    if city is not None and dateRange is not None:
        for record in data:
            if record['City'] == city and (record['Date'] >= dateRange[0] and record['Date'] <= dateRange[1]):
                result.append(record)
    elif city is not None and dateRange is None:
        for record in data:
            if record['City'] == city:
                result.append(record)
    elif city is None and dateRange is not None:
        for record in data:
            if record['Date'] >= dateRange[0] and record['Date'] <= dateRange[1]:
                result.append(record)
    else:
        return data
    return result


def printFormat(record):
    return f"{record['City']}, {record['Country']} ({record['Date']}): \n" + \
           f"\t Temperature: {record['Temperature']} °C \n" + \
           f"\t Умови: {record['Conditions']}"


def getRecordWithMinProperty(data, propertyName, city=None, dateRange=None):
    dataByRange = getByCityAndDateRange(data, city, dateRange)
    minRecord = dataByRange[0]
    for record in dataByRange:
        if minRecord[propertyName] > record[propertyName]:
            minRecord = record
    return minRecord


def getRecordWithMaxProperty(data, propertyName, city=None, dateRange=None):
    dataByRange = getByCityAndDateRange(data, city, dateRange)
    maxRecord = dataByRange[0]
    for record in dataByRange:
        if maxRecord[propertyName] < record[propertyName]:
            maxRecord = record
    return maxRecord


def getAverageByProperty(data, propertyName, city=None, dateRange=None):
    average = 0.0
    dataByRange = getByCityAndDateRange(data, city, dateRange)
    if len(dataByRange) > 0:
        for record in dataByRange:
            average += record[propertyName]
        return average / len(dataByRange)
    else:
        return 0


def getRecordsWherePropertyLessThan(data, propertyName, value, dateRange=None):
    dataByRange = getByCityAndDateRange(data, None, dateRange)
    result = []
    for record in dataByRange:
        if record[propertyName] < value:
            result.append(record)
    return result


def getRecordsWherePropertyMoreThan(data, propertyName, value, dateRange=None):
    dataByRange = getByCityAndDateRange(data, None, dateRange)
    result = []
    for record in dataByRange:
        if record[propertyName] > value:
            result.append(record)
    return result


def getRecordsWherePropertyEqual(data, propertyName, value, dateRange=None):
    dataByRange = getByCityAndDateRange(data, None, dateRange)
    result = []
    for record in dataByRange:
        if record[propertyName] == value:
            result.append(record)
    return result


def printHelp():
    print('Для старту введіть одну з перелічених команд\n' +
          '\t 1)stop - для зупинки виконання.\n' +
          '\t 2)city_date <city> <date> - Пошук погоди в певному місті на певну дату.\n' +
          '\t 3)min_temperature <dateFrom> <dateTo> - знаходить найменшу температуру на проміжку часу від dateFrom до dateTo (можна вказати лише dateFrom).\n' +
          '\t 4)max_temperature <dateFrom> <dateTo> - знаходить найбільшу температуру на проміжку часу від dateFrom до dateTo (можна вказати лише dateFrom).\n' +
          '\t 5)temperature_dynamics <city> <dateFrom> <dateTo> - показує динаміку зміни температури в певному місті на проміжку часу від dateFrom до dateTo (можна вказати лише dateFrom).\n' +
          '\t 6)temperature_less_than <value> - знаходить міста в яких температура менша ніж value' +
          '\t 7)temperature_more_than <value> - знаходить міста в яких температура більша ніж value' +
          'Формат дати повинен бути наступним День/Місяць/Рік' +
          '\nДоступні міста: Lviv, Paris\n')


def inputCommand():
    return input("Будь ласка введіть команду:\n").split(' ')


def printToFile(outputFilePath, line):
    file = open(outputFilePath, 'a', encoding='utf-8')
    print(line)
    file.write(line + '\n')
    file.close()


def main():
    data = getData('Weather.csv')

    printHelp()

    file = open("test_result.txt", 'w', encoding='utf-8')
    file.close()

    command = inputCommand()
    while command[0] != 'stop':
        if command[0] == 'city_date':
            if len(command) == 1:
                result = getByCityAndDate(data)
            elif len(command) == 2:
                result = getByCityAndDate(data, command[1])
            elif len(command) == 3:
                result = getByCityAndDate(data, command[1], datetime.datetime.strptime(command[2], '%d/%m/%Y'))
            for record in result:
                print(printFormat(record))
                printToFile("test_result.txt", printFormat(record))
        elif command[0] == 'min_temperature':
            if len(command) == 1:
                record = getRecordWithMinProperty(data, 'Temperature')
                printToFile("test_result.txt", f'Minimum temperature ({record["Temperature"]} °C) in the city {record["City"]}')
                print(f'Minimum temperature ({record["Temperature"]} °C) in the city {record["City"]}')
            elif len(command) == 2:
                dateFrom = datetime.datetime.strptime(f'{command[1]} 00:00', '%d/%m/%Y %H:%M')
                dateTo = datetime.datetime.strptime(f'{command[1]} 23:00', '%d/%m/%Y %H:%M')
                record = getRecordWithMinProperty(data, 'Temperature', None, [dateFrom, dateTo])
                print( f'Minimum temperature ({record["Temperature"]} °C) on the interval from {command[1]} 00:00 to {command[1]} 23:00 in the city {record["City"]}')
                printToFile("test_result.txt", f'Minimum temperature ({record["Temperature"]} °C) on the interval from {command[1]} 00:00 to {command[1]} 23:00 in the city {record["City"]}')
            elif len(command) == 3:
                dateFrom = datetime.datetime.strptime(f'{command[1]} 00:00', '%d/%m/%Y %H:%M')
                dateTo = datetime.datetime.strptime(f'{command[2]} 23:00', '%d/%m/%Y %H:%M')
                record = getRecordWithMinProperty(data, 'Temperature', None, [dateFrom, dateTo])
                print(f'Minimum temperature ({record["Temperature"]} °C) on the interval from {command[1]} 00:00 to {command[2]} 23:00 in the city {record["City"]}')
                printToFile("test_result.txt", f'Minimum temperature ({record["Temperature"]} °C) on the interval from {command[1]} 00:00 to {command[2]} 23:00 in the city {record["City"]}')
        elif command[0] == 'max_temperature':
            if len(command) == 1:
                record = getRecordWithMaxProperty(data, 'Temperature')
                print(f'Maximum temperature ({record["Temperature"]} °C) in the city {record["City"]}')
                printToFile("test_result.txt",f'Maximum temperature ({record["Temperature"]} °C) in the city {record["City"]}')
            elif len(command) == 2:
                dateFrom = datetime.datetime.strptime(f'{command[1]} 00:00', '%d/%m/%Y %H:%M')
                dateTo = datetime.datetime.strptime(f'{command[1]} 23:00', '%d/%m/%Y %H:%M')
                record = getRecordWithMaxProperty(data, 'Temperature', None, [dateFrom, dateTo])
                print(f'Maximum temperature ({record["Temperature"]} °C) on the interval from {command[1]} 00:00 to {command[1]} 23:00 in the city {record["City"]}')
                printToFile("test_result.txt",f'Maximum temperature ({record["Temperature"]} °C) on the interval from {command[1]} 00:00 to {command[1]} 23:00 in the city {record["City"]}')
            elif len(command) == 3:
                dateFrom = datetime.datetime.strptime(f'{command[1]} 00:00', '%d/%m/%Y %H:%M')
                dateTo = datetime.datetime.strptime(f'{command[2]} 23:00', '%d/%m/%Y %H:%M')
                record = getRecordWithMaxProperty(data, 'Temperature', None, [dateFrom, dateTo])
                print( f'Maximum temperatureа ({record["Temperature"]} °C) on the interval from {command[1]} 00:00 to {command[2]} 23:00 in the city {record["City"]}')
                printToFile("test_result.txt", f'Maximum temperature ({record["Temperature"]} °C) on the interval from {command[1]} 00:00 to {command[2]} 23:00 in the city {record["City"]}')

        elif command[0] == 'temperature_dynamics':
            result = []
            if len(command) == 2:
                result = getByCityAndDateRange(data, command[1])
            elif len(command) == 3:
                dateFrom = datetime.datetime.strptime(f'{command[2]} 00:00', '%d/%m/%Y %H:%M')
                dateTo = datetime.datetime.strptime(f'{command[2]} 23:00', '%d/%m/%Y %H:%M')
                result = getByCityAndDateRange(data, command[1], [dateFrom, dateTo])
                print( f"The dynamics will change the temperature in the city {command[1]} as of {command[2]}:")
                printToFile("test_result.txt", f"The dynamics will change the temperature in the city {command[1]} as of {command[2]}:")
            elif len(command) == 4:
                dateFrom = datetime.datetime.strptime(f'{command[2]} 00:00', '%d/%m/%Y %H:%M')
                dateTo = datetime.datetime.strptime(f'{command[3]} 23:00', '%d/%m/%Y %H:%M')
                result = getByCityAndDateRange(data, command[1], [dateFrom, dateTo])
                print(f"The dynamics will change the temperature in the city {command[1]} з {command[2]} 00:00 to {command[3]} 23:00:")
                printToFile("test_result.txt",f"The dynamics will change the temperature in the city {command[1]} from {command[2]} 00:00 to {command[3]} 23:00:")
            temperatureRecords = []
            for record in result:
                temperatureRecords.append(str(record["Temperature"]))
            print('°C '.join(temperatureRecords) + '°C')
            printToFile("test_result.txt", '°C '.join(temperatureRecords) + '°C')
        elif command[0] == 'temperature_less_than':
            if len(command) == 2:
                result = getRecordsWherePropertyLessThan(data, 'Temperature', float(command[1]))
                resultCities = []
                for record in result:
                    resultCities.append(record['City'])
                print(f'Temperature is less than {command[1]} °C in cities: ' + ', '.join(list(set(resultCities))))
                printToFile("test_result.txt",f'Temperature is less than {command[1]} °C in cities: ' + ', '.join(list(set(resultCities))))
        elif command[0] == 'temperature_more_than':
            if len(command) == 2:
                result = getRecordsWherePropertyMoreThan(data, 'Temperature', float(command[1]))
                resultCities = []
                for record in result:
                    resultCities.append(record['City'])
                print(f'Temperature bigger than {command[1]} °C in cities: ' + ', '.join(list(set(resultCities))))
                printToFile("test_result.txt", f'Temperature bigger than {command[1]} °C in cities: ' + ', '.join(list(set(resultCities))))
        else:
            print("Invalid command, try again")
        command = inputCommand()


if __name__ == '__main__':
    main()
