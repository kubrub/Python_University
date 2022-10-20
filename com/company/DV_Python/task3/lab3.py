def getData(fileName):
    """Get data from file

    fileName - path to file

    trumDirection is: forward, backward

    Data input format must be:
        tramNumber-trumDirection:stop1-stop2-stop3-...

    Data output format is:
    {'tramNumber':
        {
            'forward': [stop1, stop2, stop3],
            'backward': [...]
        },
     'otherTramNumber':
        {
            'forward': [...],
            'backward': [...]
        },
     ...
    }
    """
    data = {}
    file = open(fileName, 'r', encoding='utf-8')
    lines = file.read().split('\n')
    for line in lines:
        splitedRow = line.split(':')
        splitedStops = splitedRow[1].split('–')
        splitedInfo = splitedRow[0].split('–')
        if data.get(splitedInfo[0]):
            data[splitedInfo[0]].update({splitedInfo[1]: splitedStops})
        else:
            data[splitedInfo[0]] = {splitedInfo[1]: splitedStops}
    return data


def prettyPrint(data, routeNumber):
    """Pretty print tram route

    route - tram route
    """
    if routeNumber in data:
        route = data[routeNumber]
        print(f'Вперед:')
        for stop in route['forward']:
            print(f'\t{stop}')
        print(f'Назад:')
        for stop in route['backward']:
            print(f'\t{stop}')
    else:
        print(f'У Львові немає трамвая з таким номером')


def getTramsOnStation(data, station):
    """Get all trams which stop on this station

    data - list of all tram routes
    station - name of station
    """
    trams = []
    for record in data:
        if station in data[record]['forward'] or station in data[record]['backward']:
            trams.append(record)
    return trams


def getIntersection(data, tram1, tram2):
    """Get intersection of tram1 and tram2 routes

    data - list of all tram routes
    tram1 - identifier of the first tram
    tram2 - identifier of the second tram
    """
    stations = None
    if tram1 in data and tram2 in data:
        stations = {}
        stations['forward'] = [value for value in data[tram1]['forward'] if value in data[tram2]['forward']]
        stations['backward'] = [value for value in data[tram1]['backward'] if value in data[tram2]['backward']]
    return stations


def getNumberOfStation(data, station1, station2):
    """Get number of station from station1 to station2 without tram change

    data - list of all tram routes
    station1 - name of start station
    station1 - name of end station

    return: number of station, route
    """
    if station1 == station2:
        return 0
    tram = None

    for route in data:
        if station1 in data[route]['forward'] and station2 in data[route]['forward']:
            station1Index = data[route]['forward'].index(station1)
            station2Index = data[route]['forward'].index(station2)
            if station1Index < station2Index:
                number = abs(station1Index - station2Index)
                tram = route

        if station1 in data[route]['backward'] and station2 in data[route]['backward']:
            number = abs(data[route]['backward'].index(station1) - data[route]['backward'].index(station2))
            tram = route
    if tram is not None:
        return number, tram
    else:
        return None


def getNumberOfStationAtRoute(route, station1, station2):
    """Get number of station from station1 to station2 in route

    data - tram route
    station1 - name of start station
    station1 - name of end station

    return: number of station
    """
    if station1 in route['forward'] and station2 in route['forward']:
        station1Index = route['forward'].index(station1)
        station2Index = route['forward'].index(station2)
        return abs(station1Index - station2Index)
    else:
        station1Index = route['backward'].index(station1)
        station2Index = route['backward'].index(station2)
        return abs(station1Index - station2Index)


def getRoute(data, station1, station2):
    """Get route from station1 to station2

    data - list of all tram routes
    station1 - name of start station
    station1 - name of end station

    if without station change
        return: number of station, route
    if with station change
        return list of [first route number, second route number, intersect station, first route length, second route length]
    """

    trams = []
    route = getNumberOfStation(data, station1, station2)
    if route is not None:
        return route
    else:
        firstStationTrams = []
        secondStationTrams = []
        for route in data:
            if station1 in data[route]['forward'] or station1 in data[route]['backward']:
                firstStationTrams.append(route)

            if station2 in data[route]['forward'] or station2 in data[route]['backward']:
                secondStationTrams.append(route)

        firstLength = 0
        secondLength = 0
        for i in range(len(firstStationTrams)):
            for j in range(len(secondStationTrams)):
                intersectStations = getIntersection(data, firstStationTrams[i], secondStationTrams[j])
                if len(intersectStations['forward']) != 0 or len(intersectStations['backward']) != 0:
                    firstLength = getNumberOfStation(data, station1, intersectStations['backward'][0])[0]
                    secondLength = getNumberOfStation(data, intersectStations['backward'][0], station2)[0]
                    intersectStation = intersectStations['backward'][0]
                    for station in intersectStations['backward']:
                        tempLength = getNumberOfStation(data, station1, station)
                        if tempLength is not None and tempLength[0] < firstLength:
                            firstLength = getNumberOfStationAtRoute(data[firstStationTrams[i]], station1, station)
                            secondLength = getNumberOfStationAtRoute(data[secondStationTrams[j]], station, station2)
                            intersectStation = station
                    for station in intersectStations['forward']:
                        tempLength = getNumberOfStation(data, station1, station)
                        if tempLength is not None and tempLength[0] < firstLength:
                            firstLength = getNumberOfStationAtRoute(data[firstStationTrams[i]], station1, station)
                            secondLength = getNumberOfStationAtRoute(data[secondStationTrams[j]], station, station2)
                            intersectStation = station

                    trams.append(
                        [firstStationTrams[i], secondStationTrams[j], intersectStation, firstLength, secondLength])
        if len(trams) != 0:
            return trams
        else:
            return None


def inputCommand():
    """Process command entering"""
    return input("Будь ласка введіть команду:\n").split(';')


def commandsMenu():
    print()
    print("1)stop - для зупинки виконання.")
    print("2)get_route;<route number> - Виводить маршрут за номером. "
          "\n\tПриклад команди:\n\t\tget_route;8")
    print("3)station;<station name> - Виводить маршрути, що проїжджають крізь задану зупинку."
          "\n\tПриклад команди:	\n\t\tstation;Театр ляльок")
    print("4)intersect;<first route number>;<second route number> - знаходить зупинки на яких трамваї перетинаються."
          "\n\tПриклад команди: \n\t\tintersect;3;8")
    print("5)length;<first station name>;<second station name> - знаходить мінімальний шлях між зупинками, якщо \nвони знаходяться на одному маршруті."
          "\n\tПриклад команди: \n\t\tlength;Аквапарк;вул. Сахарова")
    print("6)find_route;<first station name>;<second station name> - Знаходить яким(якими) трамваєм(трамваями) можна доїхати з однієї зупинки до іншої (можлива одна пересадка)."
          "\n\tПриклад команди: \n\t\tfind_route;Аквапарк;вул. Сахарова")
    print()


def main():
    data = getData('routes.txt')
    #     print(data)
    commandsMenu()
    command = inputCommand()

    while command[0] != 'stop':
        if command[0] == 'get_route':
            #             ## command example: get_route;8
            prettyPrint(data, command[1])

        elif command[0] == 'station':
            #             ## command example: station;Театр ляльок
            tramsNumbers = getTramsOnStation(data, command[1])
            print(f'Через зупинку "{command[1]}" проїжджають трамваї №: {", ".join(tramsNumbers)}' if len(
                tramsNumbers) > 0 else f'Жоден трамвай не їде через зупинку "{command[1]}"')

        elif command[0] == 'intersect':
            #             ## command example: intersect;3;8
            intersection = getIntersection(data, command[1], command[2])
            if intersection is None:
                print(f'Одного з трамвайних маршрутів {command[1]}, {command[2]} не існує.')
            elif len(intersection['forward']) == 0 and len(intersection['backward']) == 0:
                print(f'Трамвайні маршрути {command[1]} та {command[2]} не перетинаються.')
            else:
                print(f'Трамвайні маршрути {command[1]} та {command[2]} перетинаються:')
                print(f'\t Вперед: {", ".join(intersection["forward"])}' if len(
                    intersection['forward']) > 0 else '\t Не перетинаються вперед')
                print(f'\t Назад: {", ".join(intersection["backward"])}' if len(
                    intersection['backward']) > 0 else '\t Не перетинаються назад')

        elif command[0] == 'length':
            #             ## command example: length;Аквапарк;вул. Сахарова
            result = getNumberOfStation(data, command[1], command[2])
            print(
                f'Кількість зупином між станціями "{command[1]}" та "{command[2]}" - {result[0]}, трамвай №{result[1]}' if result is not None else "Зупинки не знаходяться на одному маршруті")

        elif command[0] == 'find_route':
            #             ## command example: find_route;Аквапарк;вул. Сахарова
            #             ## command example: find_route;Аквапарк;стадіон «Україна»
            routes = getRoute(data, command[1], command[2])
            if routes is not None:
                if type(routes[0]) == int:
                    print(
                        f'Зі станції "{command[1]}" до стандії "{command[2]}" можна добратися трамваєм №{routes[1]} (к-сть зупинок {routes[0]})')
                else:
                    for variant in routes:
                        print(
                            f'{routes.index(variant) + 1}) Щоб добратися зі станції "{command[1]}" до стандії "{command[2]}" необхідно спочатку сісти на трамвай №{variant[0]} ' +
                            f'(к-сть зупинок {variant[3]}), а потім пересісти на трамвай №{variant[1]} на зупинці "{variant[2]}" (к-сть зупинок {variant[4]})')
            else:
                print("Скористайтесь іншим видом транспорту")

        else:
            print("Невірна команда спробуйте ще раз")
        commandsMenu()
        command = inputCommand()


if __name__ == '__main__':
    main()
