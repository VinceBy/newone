class Queue():
    """队列"""
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        """往队列中添加一个ｉｔｅｍ元素"""
        self.__list.append(item)

    def dequeue(self):
        """从队列头部删除一个元素"""
        return self.__list.pop(0)

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.__list == []

    def size(self):
        """判断队列的长度"""
        return len(self.__list)


if __name__ == "__main__":
    s = Queue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())