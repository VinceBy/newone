class Deque():
    """双端队列"""
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        """往队列中头部添加一个ｉｔｅｍ元素"""
        self.__list.insert(0,item)

    def add_rear(self, item):
        """从队列尾部删除一个元素"""
        self.__list.append(item)

    def pop_front(self):
        """从头部取"""
        return self.__list.pop(0)
    def pop_rear(self):
        """从尾部取"""
        return self.__list.pop()

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.__list == []

    def size(self):
        """判断队列的长度"""
        return len(self.__list)

if __name__ =="__main__":
    s = Deque()
    s.add_front(1)
    print(s.pop_front())



