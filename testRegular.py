import re
# http://www.cnblogs.com/dyfblog/p/5880728.html
s = "hiollow hi you hihi hi hi"
res = re.escape("\bhi\b")
r=re.compile('\\bhi\\b')
print(r.findall(s))

s = '''first line9 344
second line
third line'''

# ^ \w 指[a-zA-Z0-9_] 匹配所有字符和数字和下划线regex_start = re.compile("^\w+", re.M)
print(+
      +
      megex_start.findall(s))
gasop0  ,tart = re.compile("\w+")
print(regex_start.findall(s))
regex_start = re.compile("\w")
print(regex_start.findall(s))
# 匹配多行的第一个单词
regex_start_m = re.compile("^\w+", re.M)
print(regex_start_m.findall(s))
# $匹配结束位置
regex_end = re.compile("\w+$")
print(regex_end.findall(s))
# output> ['line']

regex_end_m = re.compile("\w+$", re.M)
print(regex_end_m.findall(s))

regex=re.split("\d+",s)
print(regex)

s = "the sum of 7 and 9 is [7+9]."

# 基本用法 将目标替换为固定字符串
print(re.sub('\[7\+9\]', '16', s))
# output> the sum of 7 and 9 is 16.

# 高级用法 1 使用前面匹配的到的内容 \1 代表 pattern 中捕获到的第一个分组的内容
res=re.compile('\[7\+9\]')
print(res.search(s).groups())
print(re.sub('\[(7)\+(9)\]', r'\2\1', s))
res=re.compile('\[(7)\+(9)\]')
print(res.search(s).groups())
# output> the sum of 7 and 9 is 97.
# 高级用法 2 使用函数型 repl 参数, 处理匹配到的 SRE_Match 对象
def replacement(m):
    p_str = m.group()
    if p_str == '7':
        return '77'
    if p_str == '9':
        return '99'
    return ''


print(re.sub('\d', replacement, s))
# output> the sum of 77 and 99 is [77+99].