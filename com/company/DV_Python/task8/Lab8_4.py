import xml.etree.ElementTree as ElementTree
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


def xmlResultParse(filename):
    logger.info("Parse xml file and print result")
    logger.info("get xml file")
    tree = ElementTree.parse(filename)
    logger.info("get xml file root element")
    root = tree.getroot()
    total = 0

    logger.info("Print all seller:")
    for listing in root.findall('listing'):
        sellerInfo = listing.find('seller_info')
        sellerName = sellerInfo.find('seller_name').text
        sellerRating = sellerInfo.find('seller_rating').text
        logger.info(f"{sellerName} - {sellerRating}")
        total += 1
    logger.info(f"\nTotal seller: {total}\n")

    logger.info("Get all auction info:")
    auctionInfos = dict()
    for auctionInfo in root.findall('.//auction_info'):
        idNum = auctionInfo.find('id_num').text
        location = auctionInfo.find('location').text
        auctionInfos[idNum] = location
    for idNum in auctionInfos.keys():
        logger.info(f"{idNum} - {auctionInfos[idNum]}")


def main():
    xmlResultParse('xmlResult.xml')


if __name__ == "__main__":
    main()
