class Node():
    def __init__(self,elem):
        "单链表节点"
        self.elem = elem
        self.next = None
        self.prev = None
class DoubleLinkList():
    "单链表"
    def __init__(self,node=None):
        self.__head = node

    def is_empyt(self):
        "链表是否为空"
        return self.__head == None

    def length(self):
        "链表的长度"
        #cur游标，用来移动遍历节点
        cur = self.__head
        #count 记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        "遍历整个链表"
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self,item):
        "链表头部添加元素　头插法"
        node = Node(item)
        node.next = self.__head
        self.__head = node
        node.next.prev = node
    def append(self,item):
        "链表的尾部添加尾插发"
        node = Node(item)
        if self.is_empyt():#判断链表是否为空
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

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
            cur = self.__head
            count = 0
            while count < pos:
                cur = cur.next
                count += 1
            #当循环退出后，ｐｒｅ指向ｐｏｓ－１
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self,item):
        "删除指定位置的元素"
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                #先判断此节点是否是头结点
                #头结点
                if cur == self.__head:
                    self.__head = cur.next#此处不可以是ｃｕｒ
                    if cur.next:#判断链表是否只有一个节点
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:#判断要删除的元素是否是最后一个元素
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next

    def search(self, item):
        "查找节点是否存在"
        node = Node(item)
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

if __name__  == "__main__":
    ll = DoubleLinkList()
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
    ll.append(6)
    # ll.travel()
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








