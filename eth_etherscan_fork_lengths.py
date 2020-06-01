import requests
import cfscrape
from bs4 import BeautifulSoup
from collections import OrderedDict


URL = "https://etherscan.io/blocks_forked?p="


def getData(scraper, page):
    url = URL + page
    print("Retrieving page", page)
    return BeautifulSoup(scraper.get(url).content, 'html.parser')


def getPage(scraper, page):
    table = getData(scraper, str(page)).find('table')
    return [[X.text.strip() for X in row.find_all('td')] for row in table.find_all('tr')]


def main():
    #session = requests.Session()
    scraper = cfscrape.create_scraper()
    counts = OrderedDict()

    page = 0
    while page < 1000:
        page += 1
        data = getPage(scraper, page)

        try:
            for item in data:
                if len(item) != 0:
                    if item[9] in counts:
                        counts[item[9]] += 1
                    else:
                        counts[item[9]] = 1
        except:
            break

    for k, v in counts.items():
        print("Forks of length {}: {}".format(k, v))


if __name__ == "__main__":
    main()
