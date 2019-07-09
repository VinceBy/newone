# 第四节链表　０３　
class Node():
    def __init__(self,elem):
        "单链表节点"
        self.elem = elem
        self.next = None
class SingleCycleLinkList():
    "单项循环链表"
    def __init__(self,node=None):
        self.__head = node
        if node:
            node.next = node
    def is_empyt(self):
        "链表是否为空"
        return self.__head == None

    def length(self):
        "链表的长度"
        if self.is_empyt():
            return 0
        #cur游标，用来移动遍历节点
        cur = self.__head
        #count 记录数量
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        "遍历整个链表"
        if self.is_empyt():
            return None

        cur = self.__head
        while cur.next !=self.__head:
            print(cur.elem, end=" ")
            cur = cur.next
        #退出循环，ｃｕｒ指向为节点，但是尾节点的元素为打印
        print(cur.elem)

    def add(self,item):
        "链表头部添加元素　头插法"
        node = Node(item)
        if self.is_empyt():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next !=self.__head:
                cur = cur.next
            #退出循环，ｃｕｒ指向尾节点
            node.next = self.__head
            self.__head = node
            # cur.next = node
            cur.next = self.__head
    def append(self,item):
        "链表的尾部添加 尾插法"
        node = Node(item)
        if self.is_empyt():#判断链表是否为空
            self.__head = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def insert(self,pos,item):
        """
        指定位置添加元素
        :parm pos 从0开始
        """
        if pos<=0:
            self.add(item)
        elif pos>self.length()-1:
            self.append(item)
        else:
            node = Node(item)
            pre = self.__head
            count = 0
            while count < (pos-1):
                pre = pre.next
                count += 1
            #当循环退出后，ｐｒｅ指向ｐｏｓ－１
            node.next = pre.next
            pre.next = node#这里出过错误 node 是一个指向堆的指向

    def remove(self,item):
        "删除指定位置的元素"
        if self.is_empyt():
            return
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.elem == item:
                #先判断此节点是否是头结点
                #头结点
                if cur == self.__head:
                    # 头结点
                    # 找尾节点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next#此处不可以是ｃｕｒ　
                    rear.next = self.__head
                else:
                    # 中间节点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        # 退出循环，ｃｕｒ指向尾节点
        if cur.elem == item:
            if cur == self.__head:
                #链表只有一个节点
                self.__head = None
            else:
                # pre.next = cur.next
                pre.next = self.__head
    def search(self, item):
        "查找节点是否存在"
        if self.is_empyt():
            return False
        node = Node(item)
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        #退出循环，ｃｕｒ指向尾节点
        if cur.elem == item:
            return True
        else:
            return False
        return False

if __name__  == "__main__":
    ll = SingleCycleLinkList()
    print(ll.is_empyt())
    print(ll.length())
    ll.append(1)
    print(ll.is_empyt())
    print(ll.length())
    ll.append(2)
    ll.append(3)
    ll.add(8)

    ll.append(4)
    ll.append(5)
    ll.travel()
    # 812345
    ll.insert(-1,9) #9812345
    ll.travel()
    ll.insert(3,100) #9 8 1 100 2 3 4 5
    ll.travel()
    ll.insert(10,200)# 9 8 1 100 2 3 4 5  200
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel()








