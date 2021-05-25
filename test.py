from bs4 import BeautifulSoup
import codecs
import pandas as pd
import openpyxl     

htmlFileNames = ['html/tricycle/' + str(x) + '.html' for x in range(4)]
# print(htmlFileNames)
deal_cnt = []
price = []
title = []
link = []
result = pd.DataFrame(columns=('title', 'link', 'price', 'deal_cnt'))
# result['title'] = ''
# result['link'] = ''
# result['price'] = ''
# result['deal_cnt'] = ''
# new = result
for path in htmlFileNames:
    # print(path)
    # htmlFile = open(path, 'r', encoding='utf-8')
    # htmlHandle = htmlFile.read()
    soup = BeautifulSoup(codecs.open(path, 'r', encoding='utf-8'), 'lxml')
    items = soup.find_all(class_='ctx-box')
    for item in items:
        new = {}
        # 月销量
        # print(item.find(class_='deal-cnt').get_text().strip()[:-3])
        new['deal_cnt'] = item.find(class_='deal-cnt').get_text().strip()[:-3]

        # 价格
        # print(item.find(class_='price').get_text().strip()[1:])
        new['price'] = item.find(class_='price').get_text().strip()[1:]

        # 标题
        # print(item.find(class_='J_ClickStat').get_text().strip())
        new['title'] = item.find(class_='J_ClickStat').get_text().strip()

        # 链接
        # print(item.find(class_='J_ClickStat')['href'].strip()[2:])
        new['link'] = item.find(class_='J_ClickStat')['href'].strip()[2:]

        # print(new)
        result = result.append(new,ignore_index=True)
        # break
# print(result)
result.to_excel("test.xlsx",engine='openpyxl')