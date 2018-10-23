from pyquery import PyQuery as pq
import pandas as pd

# import urllib3
# page = urllib3.("http://example")
# text = unicode(page.read(), "utf-8")
# import sys
#
# print(sys.getdefaultencoding())
# file = open('zcw众彩网\\18122.html', 'w', encoding='utf-8')
# file
htmlf = open('111.html', 'r', encoding="utf-8")
htmlcont = htmlf.read()
# print(htmlcont)
doc = pq(htmlcont)
# print(doc)
section = doc('section')('[data-id=\'2660\']')


def getData():
    ss = s[s.index('：') + 1:]
    if ss.__contains__("、"):
        return ss.split("、")
    elif ss.__contains__(" "):
        return ss.split(" ")


# print(section)
for item in section.items():
    name = item('p')(
        '[style="padding-right: 20px;padding-left: 20px;font-size: 16px;color: inherit;border-color: rgb(166, 91, 203);"]').text()
    p = item('span')('[style="font-size: 15px;color: rgb(255, 104, 39);"]')
    print(name)
    first = p.eq(0)
    s = first.text()

    print(s)
    if s.__contains__('：'):
        print(s[s.index('：') + 1:])
        data = getData()
        print(data)
        se = pd.Series(data)
        print(se)
    # for span in p.items():
    #     s = span.text()
    #     # s = span.text()
    #     print(s)
    # if s.__contains__('：'):
    # print(s[s.index('：') + 1:])
    # data = getData()
    # print(data)
    # se = pd.Series(data)
    # print(se)

# if item.attr('data-id') == '2660':
#     print(item)
#     span = item('[style=font-size: 15px;color: rgb(255, 104, 39)]')
#     for spanItem in span.items():
#         if spanItem.attr("style") == 'font-size: 15px;color: rgb(255, 104, 39);':
#             print(span)

# doc
