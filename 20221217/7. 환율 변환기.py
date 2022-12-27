import requests
# python3 이상은 BeautifulSoup4 설치하기!
# pip install BeautifulSoup4
from bs4 import BeautifulSoup


def get_exchange_rate(target1, target2):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
        'Referer': 'https://kr.investing.com/currencies',
        'Content-Type': 'text/html; charset=utf-8'
    }

    url = f'https://obank.kbstar.com/quics?page=C101422&monyCd=USD#CP'
    print(url)
    response = requests.get(url, headers=headers)
    print(response.reason)
    print(response.status_code)
    content = BeautifulSoup(response.content, 'html.parser')
    containers = content.find('span', {'data-test': 'instrument-price-last'})
    print(containers)
    #print(containers.text)

get_exchange_rate('usd', 'krw')

