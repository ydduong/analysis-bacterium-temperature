# encoding = utf-8
"""
test signal thread spider
"""
import sys

import requests
from lxml import etree
from bs4 import BeautifulSoup

url = [
    "https://www.shanghairanking.cn/rankings/bcur/2021",
    "https://webshop.dsmz.de/en/bacteria/Octadecabacter-antarcticus.html?listtype=search&searchparam=Octadecabacter",
    "https://webshop.dsmz.de/en/bacteria/Roseivirga-ehrenbergii.html?listtype=search&searchparam=Roseivirga%20ehrenbergii",
    "https://webshop.dsmz.de/index.php?lang=1&cl=search&searchparam=Camelimonas+lactis",
    "https://webshop.dsmz.de/index.php?lang=1&cl=search&searchparam=Caldisericales+bacterium",
    "https://webshop.dsmz.de/index.php?lang=1&cl=search&searchparam=Legionella",
    "https://www.dsmz.de/search?tx_kesearch_pi1%5Bsword%5D=Nitrosomonas%C2%A0eutropha",
    "https://www.dsmz.de/search?tx_kesearch_pi1%5Bsword%5D=Vibrio%20qinghaiensis"
]

headers = {
    'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
}
# resp = ""


def get_html(_url, _headers):
    print(f'_url:{_url}')
    try:
        resp = requests.get(url=_url, headers=_headers, timeout=(6.05, 30))  # 发出请求
        resp.encoding = resp.apparent_encoding
        if resp.status_code == 200:
            print(f'url is right')
            return resp.text
    except Exception as e:
        print("地址({0})出错：{1}".format(_url, e))


"""
# print(resp.text)
resp_html = etree.HTML(get_html(url[0], headers))
target_url_list = resp_html.xpath('//*[@id="searchList"]/div/div/form/div[2]/div[2]/div/div[6]/div/a/@href')
target_url = ''

if len(target_url_list) > 0:
    print(target_url_list[0])
    target_url = target_url_list[0]
else:
    print('target url is none')
    sys.exit(1)
"""
target_url = url[0]
text = get_html(target_url, headers)
soup = BeautifulSoup(text, "html.parser")
td_list = soup.find_all("td")
# print(tr_list)
num = 0
nun1 = 0
print(len(td_list))
for item in td_list:
    # print(item)
    sp = BeautifulSoup(str(item), "html.parser")
    print(type(sp.a))
    if sp.a is not None:
        print(sp.a.string)
    a = sp.a
    # print()
    # print(a.string)
    print("-----------------")
    # print(tr.descendants)
    # for j in soup.find('tr').descendants:
    #     print(j.string)
    #     print('+++++++++++++++++++++++++++')
    #
    num += 1
    if num == 3:
        break

##################################
# # print(f"{text}")
# info_index = text.find('&deg;C')
# print(info_index)
# print(text[info_index-3:info_index].strip())
# if text[info_index - 2] == " ":
#     print(text[info_index-2:info_index].strip())

# print(text)
# target_url_html = etree.HTML(text)
# print(etree.tostring(target_url_html))
# # //*[@id="description"]/table/tr[12]/td[2]/text()[1]
# target_info = target_url_html.xpath['//*[@id="description"]/table']
# for item in target_info:
#     table_info = etree.tostring(item, encoding='utf-8')
#     info_index = table_info.find(b'\xc2\xb0C')
#     print(table_info[info_index-2:info_index])

# target_info = target_info[0].replace('°', ' ')
# target_info = target_info.split(' ')
# info = target_info[1]
# print(info)

# //*[@id="description"]/table/tbody/tr[12]/td[1]

