import aiohttp
import asyncio
import time
from bs4 import BeautifulSoup
from db import cur, insert_students
from random import randint

info_url = "http://xpcx.ccnu.edu.cn/page.php?cid="

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'        
}

# 文件描述符最高上限设为800
# 存到数据库中
#proxylist = ['http://120.773:1180', 'http://39.108.0:1180']
stus = []

async def getinfo(cid):
    async with aiohttp.ClientSession() as session:
        async with session.get(info_url + str(cid), headers = headers) as resp:
        # async with session.get(info_url + str(cid), proxy = proxylist[randint(0, len(proxylist)-1)]) as resp:
            soup = BeautifulSoup(await resp.text())
            content = soup.find_all('td', class_ = 'cont')
            conts = []
            for item in content:
                conts.append(item.string)
            if len(conts) != 0:
                i = cur.execute('select * from students where cid=' + conts[0])
                if i != None:
                    stu = []
                    stu.append(conts)
                    insert_students(stu, cur)

async def bound_get(sem, cid):
    async with sem:
        await getinfo(cid)

async def run(start, end):
    tasks = []
    sem = asyncio.Semaphore(100)
    for cid in range(start, end):
        task = asyncio.ensure_future(bound_get(sem, cid))
        tasks.append(task)
    resps = asyncio.gather(*tasks)
    await resps


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    #future = asyncio.ensure_future(run(2013210001, 2013214859))
    future = asyncio.ensure_future(run(2014211001, 2014212001))
    #future = asyncio.ensure_future(run(2015210001, 2015215001))
    #future = asyncio.ensure_future(run(2016210001, 2016215001))
    #future = asyncio.ensure_future(run(2017210001, 2017215001))
    loop.run_until_complete(future)
    cur.execute("SELECT COUNT(*) FROM STUDENTS;")
