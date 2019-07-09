pstr = 'hello world! ebuhfbvibuy world efbuifhsufgbeiqworldsfbfg'
#第一种方法替换字符串
def myReplace(pstr,oldStr,newStr):
    while True:
        position = pstr.find(oldStr)
        if position ==-1:
            break
        pstr = pstr[:position] + newStr + pstr[position+len(oldStr):]
    return pstr
#第二种方法
def myReplace(pstr, oldStr, newStr):
    result = pstr.split(oldSre)
    pstr = newStr.join(result)#在每个字符串的后面添加newstr 但是最后一个不加
    return pstr

a = myReplace(pstr,'world','tom')
print(a)
