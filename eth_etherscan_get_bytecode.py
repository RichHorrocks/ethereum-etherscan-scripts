#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://etherscan.io/address/"

def main():
    address = str(input("Please input an address: ").strip())
    
    url = BASE_URL + address
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    print(soup.find("div", { "id": "verifiedbytecode2" }).text)

if __name__ == "__main__":
    main()
