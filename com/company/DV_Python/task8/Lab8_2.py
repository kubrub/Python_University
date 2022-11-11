import http.client
import os
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


def get(server, url):
    logger.info(" Send get request to specific url ")
    try:
        logger.info("send get request")
        server.request('GET', url)
        logger.info("get response from server")
        response = server.getresponse()
    except:
        info = sys.exc_info()
        logger.error(info[0], info[1])
        return
    return response


def getAndWriteToFile(server, url, filename):
    logger.info("Send get request to specific url and write to file")
    logger.info("send get request")
    response = get(server, url)
    if response is None:
        logger.error("Error occurred while sending request")
    elif response.status == 200:
        logger.info("open file")
        with open(filename, "wb") as file:
            logger.info("write to file")
            file.write(response.read())
        response.close()
    else:
        logger.info("show server error")
        logger.error("Error occurred while sending request", response.status, response.reason)


def openFile(filename):
    logger.info("Open file with default setted program")
    logger.info("Get current directory")
    path = os.path.join(os.path.abspath("."), filename)
    logger.info("run file with default program")
    os.startfile(path)


def main():
    logger.info("Loading...")
    logger.info("create http client instance")
    server = http.client.HTTPSConnection("bank.gov.ua")
    filename = "test.html"
    logger.info("get response and write it to file")
    getAndWriteToFile(server, "/NBUStatService/v1/statdirectory/exchange", filename)
    logger.info("open file")
    openFile(filename)


if __name__ == "__main__":
    main()
