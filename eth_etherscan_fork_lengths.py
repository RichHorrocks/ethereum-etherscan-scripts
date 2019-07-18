import requests
from bs4 import BeautifulSoup
from collections import OrderedDict

URL = "https://etherscan.io/blocks_forked?p="

def getData(sess, page):
    url = URL + page
    print("Retrieving page", page)
    return BeautifulSoup(sess.get(url).text, 'html.parser')

def getPage(sess, page):
    table = getData(sess, str(page)).find('table')
    return [[X.text.strip() for X in row.find_all('td')] for row in table.find_all('tr')]

def main():
    resp = requests.get(URL)
    sess = requests.Session()
    
    counts = OrderedDict()

    page = 0
    while True:
        page += 1
        data = getPage(sess, page)
        
        try:
            for item in data:
                if len(item) != 0:
                    if item[8] in counts:
                        counts[item[8]] += 1
                    else:
                        counts[item[8]] = 1
        except:
            break

    for k, v in counts.items():
        print("Forks of length {}: {}".format(k, v))

if __name__ == "__main__":
    main()
