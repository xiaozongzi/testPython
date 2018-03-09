import requests
import json
#这里的header和上面的不同，大家试试看删掉一些还能不能获取数据
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
    # "DNT": "1",
    # "Host": "www.suppliercollaboration.saic-gm.com",
    # "Origin": "https://www.lagou.com",
    # "Referer": "https://www.lagou.com/jobs/list_",
    # "X-Anit-Forge-Code": "0",
    # "X-Anit-Forge-Token": None,
    # "X-Requested-With": "XMLHttpRequest" # 请求方式XHR
}

ajax_url = 'https://zhuanlan.zhihu.com/api/posts/25064739'

# first 设置为False，我们用pn来翻页，pn：表示第几页，kd：表示搜索关键字
post_param = {"first": "false", "pn": "1", "kd": "Java"}

# 使用post方式，data里面存放我们的参数，可以通过浏览器调试工具获得
r = requests.get(ajax_url, headers=headers)
print(r.content)