import requests
from bs4 import BeautifulSoup
from db import cur, insert_students
import time

info_url = "http://xpcx.ccnu.edu.cn/page.php?cid="

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
    }

def getinfo(cid):
    time.sleep(0.05)
    r = requests.get(info_url + str(cid), headers = headers)
    soup = BeautifulSoup(r.text, 'html5lib')
    content = soup.find_all('td', class_ = 'cont')
    conts = []
    for item in content:
        conts.append(item.string)
    if len(conts) != 0:
        print(conts)
        info = []
        info.append(conts)
        insert_students(info, cur)

if __name__ == '__main__':
    for cid in range(2017210001, 2017215001):
        getinfo(cid)
    for cid in range(2016210001, 2016215001):
        getinfo(cid)
    for cid in range(2015210001, 2015215001):
        getinfo(cid)
    for cid in range(2014210001, 2014215001):
        getinfo(cid)
