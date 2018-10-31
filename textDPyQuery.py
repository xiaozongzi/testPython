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
list1 = {}
alist = []
names = []
mar = []
for item in section.items():
    name = item('p')(
        '[style="padding-right: 20px;padding-left: 20px;font-size: 16px;color: inherit;border-color: rgb(166, 91, 203);"]').text()
    p = item('span')('[style="font-size: 15px;color: rgb(255, 104, 39);"]')
    # print(name)
    length = p.__len__()

    for i in range(length):
        first = p.eq(i)
        s = first.text()
        if s != '':
            break

    # print(s)
    if s.__contains__('：'):
        # print(s[s.index('：') + 1:])
        data = getData()
        data = sorted(data)
        # print(data)
        se = pd.Series(data)
        # print(se)
        if data.__len__() > 10:
            # alist.append(pd.DataFrame(se))
            # names.append(name)
            # list1[name] = se
            list1[name] = data
# result = pd.concat(alist)
# print(result)
# print(list1)
# items = list1.items()
keys = list1.keys()
for key in keys:
    mar += list1[key]
mar = sorted(mar)
print(mar)
from collections import Counter

marCount = Counter(mar)
marCountSort = sorted(marCount.items(), key=lambda x: x[1])
print(marCount.__len__())
# print(keys)
# df = pd.DataFrame(list1)
# for key in keys:
#     alist.append(df[key])
# result = pd.DataFrame(pd.concat(alist), columns=['marge'])
# group = result.sort_index(by='marge')
# print(group.sort_values)
# a = result.drop_duplicates(subset=['marge'], keep='first')
# print(a)
# for i in df.items():
#     tup=pd.DataFrame(list(i))
#     alist.append(tup)
#     # print(tup)
# result=pd.concat(alist)

# print(result)

# df['合并'] = df['唐儿'] + df['诸葛孔明']
# print(df)
# adf = pd.DataFrame(pd.Series(items))
#
# a = adf.drop_duplicates(keep='first')
# print(a)

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
