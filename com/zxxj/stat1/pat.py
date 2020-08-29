from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
if __name__ == "__main__":
    url = "http://ivdc.chinacdc.cn/cnic/zyzx/lgzb/201809/t20180902_191898.htm"
    # html = urlopen(url).read().decode('utf-8')
    r = requests.get(url, headers=headers)
    html = r.text
    soup = BeautifulSoup(html,features='lxml')
    all_span = soup.find_all('span')
    for l in all_span:
        print(l)

