import urllib.request
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


def main():
    logger.info("Loading...")
    url = "http://aiweb.cs.washington.edu/research/projects/xmltk/xmldata/data/auctions/ebay.xml"
    filename = "xmlResult.xml"
    logger.info("Get xml file")
    xmlFile = urllib.request.urlopen(url)
    logger.info("open file")
    with open(filename, "wb") as file:
        logger.info("write file")
        file.write(xmlFile.read())
    logger.info("close file")
    xmlFile.close()
    logger.info("get path")
    path = os.path.join(os.path.abspath("."), filename)
    logger.info("run file with default program")
    os.startfile(path)


if __name__ == "__main__":
    main()
