from bs4 import BeautifulSoup
import time, datetime


# 提取 快代理 网页信息，返回包含代理信息字典的列表
def handle_kuai_proxy(soup):
    proxy_list = []
    rows = soup.find_all('tr')
    for row in rows:
        proxy = {}
        cols = row.find_all('td')
        if len(cols) > 0:
            proxy['ip'] = cols[0].get_text().replace(' ', '')
            proxy['port'] = cols[1].get_text().replace(' ', '')
            proxy['location'] = cols[4].get_text().replace(' ', '')
            proxy['last_check_time'] = cols[6].get_text().replace(' ', '')
            proxy['enable'] = '1'
            proxy_list.append(proxy)
    return proxy_list


def handle_89_proxy(soup):
    proxy_list = []
    rows = soup.find_all('tr')
    for row in rows:
        proxy = {}
        cols = row.find_all('td')
        if len(cols) > 0:
            proxy['ip'] = cols[0].get_text().replace(' ', '')
            proxy['port'] = cols[1].get_text().replace(' ', '')
            proxy['location'] = cols[2].get_text().replace(' ', '')
            proxy['last_check_time'] = cols[4].get_text().replace(' ', '')
            proxy['enable'] = '1'
            proxy_list.append(proxy)
    return proxy_list
