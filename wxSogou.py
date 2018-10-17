#!/usr/bin/python
# coding: utf-8

# import sys
#
# reload(sys)
# sys.setdefaultencoding('utf-8')

from urllib.parse import quote
from pyquery import PyQuery as pq
from selenium import webdriver

import requests
import time
import re
import json
import os
import random


def get_headers():
    '''
    随机获取一个headers
    '''
    user_agents = ['Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
                   'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                   'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11']
    headers = {'User-Agent': random.choice(user_agents)}
    return headers


class weixin_spider:
    def __init__(self, kw):
        ' 构造函数 '
        self.kw = kw
        # 搜狐微信搜索链接
        # self.sogou_search_url = 'http://weixin.sogou.com/weixin?type=1&query=%s&ie=utf8&_sug_=n&_sug_type_=' % quote(self.kw)
        self.sogou_search_url = 'http://weixin.sogou.com/weixin?type=1&query=%s&ie=utf8&s_from=input&_sug_=n&_sug_type_=' % quote(
            self.kw)

        # 爬虫伪装
        self.headers = {
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 FirePHP/0refox/47.0 FirePHP/0.7.4.1'
            'User-Agent': get_headers()
        }

        # 操作超时时长
        # self.timeout = time.sleep(random.randint(0,3))
        self.s = requests.Session()

    def get_search_result_by_kw(self):
        self.log('搜索地址为：%s' % self.sogou_search_url)
        return self.s.get(self.sogou_search_url, headers=self.headers, timeout=random.randint(0, 5)).content

    def get_wx_url_by_sougou_search_html(self, sougou_search_html):
        ' 根据返回sougou_search_html，从中获取公众号主页链接 '
        doc = pq(sougou_search_html)
        # print doc('p[class="tit"]')('a').attr('href')
        # print doc('div[class=img-box]')('a').attr('href')
        # 通过pyquery的方式处理网页内容，类似用beautifulsoup，但是pyquery和jQuery的方法类似，找到公众号主页地址
        return doc('div[class=txt-box]')('p[class=tit]')('a').attr('href')

    def get_selenium_js_html(self, wx_url):
        ' 执行js渲染内容，并返回渲染后的html内容 '
        browser = webdriver.Chrome(executable_path='D:\download\chromedriver.exe')
        browser.get(wx_url)
        time.sleep(random.randint(0, 5))
        # 执行js得到整个dom
        html = browser.execute_script("return document.documentElement.outerHTML")
        return html

    def parse_wx_articles_by_html(self, selenium_html):
        ' 从selenium_html中解析出微信公众号文章 '
        doc = pq(selenium_html)
        return doc('div[class="weui_msg_card"]')

    def switch_arctiles_to_list(self, articles):
        ' 把articles转换成数据字典 '
        articles_list = []
        i = 1

        if articles:
            for article in articles.items():
                self.log(u'开始整合(%d/%d)' % (i, len(articles)))
                articles_list.append(self.parse_one_article(article))
                i += 1
            # break

        return articles_list

    def parse_one_article(self, article):
        ' 解析单篇文章 '
        article_dict = {}

        article = article('.weui_media_box[id]')

        title = article('h4[class="weui_media_title"]').text()
        self.log('标题是： %s' % title)
        url = 'http://mp.weixin.qq.com' + article('h4[class="weui_media_title"]').attr('hrefs')
        self.log('地址为： %s' % url)
        summary = article('.weui_media_desc').text()
        self.log('文章简述： %s' % summary)
        date = article('.weui_media_extra_info').text()
        self.log('发表时间为： %s' % date)
        pic = self.parse_cover_pic(article)
        content = self.parse_content_by_url(url).html()

        contentfiletitle = self.kw + '/' + title + '_' + date + '.html'
        self.save_content_file(contentfiletitle, content)

        return {
            'title': title,
            'url': url,
            'summary': summary,
            'date': date,
            'pic': pic,
            'content': content
        }

    def parse_cover_pic(self, article):
        ' 解析文章封面图片 '
        pic = article('.weui_media_hd').attr('style')

        p = re.compile(r'background-image:url\((.*?)\)')
        rs = p.findall(pic)
        self.log('封面图片是：%s ' % rs[0] if len(rs) > 0 else '')

        return rs[0] if len(rs) > 0 else ''

    def parse_content_by_url(self, url):
        ' 获取文章详情内容 '
        page_html = self.get_selenium_js_html(url)
        return pq(page_html)('#js_content')

    def save_content_file(self, title, content):
        ' 页面内容写入文件 '
        with open(title, 'w') as f:
            f.write(content.encode("gbk", 'ignore').decode("gbk", "ignore"))

    def save_file(self, content):
        ' 数据写入文件 '
        with open(self.kw + '/' + self.kw + '.txt', 'w') as f:
            f.write(content)

    def log(self, msg):
        ' 自定义log函数 '
        print
        u'%s: %s' % (time.strftime('%Y-%m-%d %H:%M:%S'), msg)

    def need_verify(self, selenium_html):
        ' 有时候对方会封锁ip，这里做一下判断，检测html中是否包含id=verify_change的标签，有的话，代表被重定向了，提醒过一阵子重试 '
        return pq(selenium_html)('#verify_change').text() != ''

    def create_dir(self):
        '创建文件夹'
        if not os.path.exists(self.kw):
            os.makedirs(self.kw)

    def run(self):
        ' 爬虫入口函数 '
        # Step 0 ：  创建公众号命名的文件夹
        self.create_dir()

        # Step 1：GET请求到搜狗微信引擎，以微信公众号英文名称作为查询关键字
        self.log(u'开始获取，微信公众号英文名为：%s' % self.kw)
        self.log(u'开始调用sougou搜索引擎')
        sougou_search_html = self.get_search_result_by_kw()

        # Step 2：从搜索结果页中解析出公众号主页链接
        self.log(u'获取sougou_search_html成功，开始抓取公众号对应的主页wx_url')
        wx_url = self.get_wx_url_by_sougou_search_html(sougou_search_html)
        self.log(u'获取wx_url成功，%s' % wx_url)

        # Step 3：Selenium+PhantomJs获取js异步加载渲染后的html
        self.log(u'开始调用selenium渲染html')
        selenium_html = self.get_selenium_js_html(wx_url)

        # Step 4: 检测目标网站是否进行了封锁
        if self.need_verify(selenium_html):
            self.log(u'爬虫被目标网站封锁，请稍后再试')
        else:
            # Step 5: 使用PyQuery，从Step 3获取的html中解析出公众号文章列表的数据
            self.log(u'调用selenium渲染html完成，开始解析公众号文章')
            articles = self.parse_wx_articles_by_html(selenium_html)
            self.log(u'抓取到微信文章%d篇' % len(articles))

            # Step 6: 把微信文章数据封装成字典的list
            self.log(u'开始整合微信文章数据为字典')
            articles_list = self.switch_arctiles_to_list(articles)

            # Step 7: 把Step 5的字典list转换为Json
            self.log(u'整合完成，开始转换为json')
            data_json = json.dumps(articles_list)

            # Step 8: 写文件
            self.log(u'转换为json完成，开始保存json数据到文件')
            self.save_file(data_json)

            self.log(u'保存完成，程序结束')


# main
if __name__ == '__main__':

    gongzhonghao = input(u'输入要爬取的公众号')
    if not gongzhonghao:
        gongzhonghao = 'python6359'
    weixin_spider(gongzhonghao).run()
