import re
pattern = "itcast"
s = "itheima"
s1 = "itcast"
result = re.match(pattern,s1)
print(dir(result))
print(result)
print(result.group())
result = re.match("itcast","itcastheima")
print(result)
print(re.match(".","i"))
re.match("...","abc")#任意匹配三个字符，不包括\n
re.match("\d","2")#匹配数字　０～９
re.match("\D","dd")#匹配非数字　不是0~9 \r:在不换行的情况下，把光标移到首位
print(re.match("\s","\ta"))#匹配空白，即空格，ｔａｂ键
re.match("\S","\nsa")#匹配非空白
re.match("\w","aaaa")#匹配单词字符,即 a~z, A~Z, 0~9, _
re.match("\W","asfasf")
print(re.match("\w\W","1@"))
print(re.match("1[358]3","183"))
re.match("1[a-z5-9]","19")
re.match("\d*","123")#匹配前一个字符出现０次或者无限次，即可有可无
re.match("\d+","abc")#匹配前一个字符一次或者无限次，即至少有一次
re.match("\d?","1234abc")#匹配前一个字符出现一次或者０次，要么有一次，要么没有
print(re.match("\d{3}[a-z]","123abc"))
re.match("\d{5}[a-z]", "1234abc")
re.match("\d{3,}[a-z]","1234abc")
re.match("\d*","a")#"a" == """a" "\d*" == ""
s = "\\nabc"
print(s)
print(re.match("\\\\n\W*",s))
s = r"\nabc"
print(s)
re.match(r"\nabc",s)
re.match(r"^$","")# ^ 匹配字符串开头　$ 匹配字符串结尾
re.match(r"1[35678]\d{9}$","hover")
print(re.match(r"^\w+\s\bve\b","ho　ve　r"))#\b 匹配一个单词的边界
print(re.match(r"^.+\bve\b","ho ve r"))
print(re.match(r"^.+\Bve\B","hover"))#\B 匹配非单词边界
re.match(r"[1-9]\d?|0$|100$","84")
print(re.match(r"[1-9]?/d?$|100$",""))
result = re.match(r"<h1>(.*)</h1>","<h1>匹配分组</h1>")
print(result.group(1))
result = re.match(r"(<h1>).*(</h1>)","<h1>匹配分组</h1>")
print(result.group(0))
print(result.groups()[0])
#  | 匹配左右任意一个表达式
# (ab)　将括号中的字符作为一个分组
# \num 引用分组num匹配到的字符串
p = r"(\w{5,20})@(163|126|qq|gmail)\.(com|cn|net)$"
r = re.match(p, "itcast@qq.com")
print(r.group())
s = "<html><h1>itcast</h1></html>"#(?P<name>) 分组其别名 (?P=name) 引用别名为ｎａｍｅ分组匹配到的字符串
print(re.match(r"<(?P<key1>.+)><(?P<key2>.+)>.+</(?P=key2)></(?P=key1)>",s))
print(re.search(r"itcast", s))
print(re.search(r"^itcast$", s))
s = "itcast</h1></html>itheima</h1>"
re.findall(r"\w+</h1>",s)
ret = re.sub(r"php","python","itcast python cpp php python php")
print(ret)
re.sub(r"\d+","python","python=1000, php=0")
def replace(result):
    print(result.group())
    r = int(result.group())+50
    return str(r)

result = re.sub(r"\d+", replace, "python=1000, php=0")
print(result)
s ="""<div>
<p>岗位职责：</p> 
<p>完成推荐算法、数据统计、接⼝、后台等服务器端相关⼯作</p> 
<p><br></p> 
<p>必备要求：</p> 
<p>良好的⾃我驱动⼒和职业素养，⼯作积极主动、结果导向</p> 
<p>&nbsp;<br></p> <p>技术要求：</p> 
<p>1、⼀年以上	Python	开发经验，掌握⾯向对象分析和设计，了解设计模式</p > 
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p> 
<p>3、掌握关系数据库开发设计，掌握	SQL，熟练使⽤	MySQL/PostgreSQL中的⼀种<br></p> 
<p>4、掌握NoSQL、MQ，熟练使⽤对应技术解决⽅案</p>
<p>5、熟悉	Javascript/CSS/HTML5，JQuery、React、Vue.js</p> 
<p>&nbsp;<br></p> <p>加分项：</p> 
<p>⼤数据，数理统计，机器学习，sklearn，⾼性能，⼤并发。</p>
</div>
"""
result = re.sub(r"</?\w+>", "", s)
print(result)
s = "itcast:php,python,cpp-java"
result = re.split(r":|,|-",s)
print(result)
s = "This is a number 135-235-44-345"
r = re.match(r"(.+?)(\d+-\d+-\d+-\d+)",s)
print(r.groups())
s = """<img	data-original="https://rpic.douyucdn.cn/appCovers/2016/1 1/13/1213973_201611131917_small.jpg"	src="https://rpic.douyuc dn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg"	st yle="display:	inline;">"""
result = re.search(r"https.+?\.jpg",s).group()
print(result)
s ="""http://www.interoem.com/messageinfo.asp?id=35 http://3995503.com/class/class09/news_show.asp?id=14 http://lib.wzmc.edu.cn/news/onews.asp?id=769 http://www.zy-ls.com/alfx.asp?newsid=377&id=6 http://www.fincm.com/newslist.asp?id=415"""


result = re.sub(r"(http://.+?/).*", lambda x: x.group(1), s)
print(result)
s = "hello world ha ha "
a = re.split(r" +",s)
print(a)
re.findall(r" \b[a-zA-Z]+\b", s)