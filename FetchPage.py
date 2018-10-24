import requests
from bs4 import BeautifulSoup

headers = {
        'Host': 'music.163.com',
        'Origin': 'https: // music.163.com',
        'Pragma': 'no-cache',
        'Referer': 'https: // music.163.com /',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }


def get_page_content(url):
    resp = requests.get(url, headers=headers)
    print(resp.content)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, 'html.parser')
        return soup
    print('服务器未返回数据')
    return None
