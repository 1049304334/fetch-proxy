import time
import random
import FetchPage
import PageContentHandler
import SaveToServer

kuai_url = 'https://www.kuaidaili.com/free/inha/'
eight_nine_url = 'http://www.89ip.cn/index_'


def start_mission():
    for pageNo in range(1, 51):
        target_url = eight_nine_url + str(pageNo) + '.html'
        print('当前url', target_url)
        content = FetchPage.get_page_content(target_url)
        if content:
            proxy_list = PageContentHandler.handle_89_proxy(content)
            for proxy in proxy_list:
                SaveToServer.save_to_db(proxy)
                print(proxy)
            print('保存了', len(proxy_list), '个代理')
        time.sleep(random.randint(10, 16))


if __name__ == '__main__':
    start_mission()
