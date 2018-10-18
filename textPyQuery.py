from pyquery import PyQuery as pq

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
section = doc('section')
# print(section)
for item in section.items():
        print(item('[data-id=\'2660\']'))

    # if item.attr('data-id') == '2660':
    #     print(item)
    #     span = item('[style=font-size: 15px;color: rgb(255, 104, 39)]')
    #     for spanItem in span.items():
    #         if spanItem.attr("style") == 'font-size: 15px;color: rgb(255, 104, 39);':
    #             print(span)

# doc
