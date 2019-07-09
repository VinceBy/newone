#下面的代码对一系列的文本做简单的文本匹配操作，当发现有匹配时就输出当前的匹配行以及最后检查的Ｎ行文本

from collections import deque

def search(lines, pattern, history=5):
    pervious_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, pervious_lines
        pervious_lines.append(line)

#Example use on a file

if __name__ =='__main__':
    with open('somefile.txt') as f:
        for line,pervlines in search(f, 'python', 5):
            for pline in pervlines:
                print(pline,end='')
            print(line, end='')
            print('-'*20)
