# coding=utf-8

# 元组
f1 = ("apple", "orange", "pear")

# 列表
f2 = ["apple", "orange", "pear"]

# 字典
f3 = {"Sam": "apple", "Jac": "orange", "mating": "pear"}


# 栈,在列表的基础上扩展
class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size
        self.top = -1

    def push(self, content):
        if self.Full():
            print("Stack is Full!")
        else:
            self.stack.append(content)
            self.top = self.top + 1

    def pop(self):
        if self.Empty():
            print("Stack is Empty!")
        else:
            self.top = self.top - 1

    def Full(self):
        if self.top == self.size:
            return True
        else:
            return False

    def Empty(self):
        if self.top == -1:
            return True
        else:
            return False


s = Stack(7)
s.Empty()
s.push("Hello")
s.pop()
s.Full()
print(s)

# 队列
class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size
        self.head = -1
        self.tail = -1

    def enQueue(self, content):
        if self.Full():
            print("Queue is Full!")
        else:
            self.queue.append(content)
            self.tail = self.tail + 1

    def outQueue(self):
        if self.Empty():
            print("Queue is Empty")
        else:
            self.tail = self.tail - 1
            self.head = self.head - 1

    def Full(self):
        if self.tail - self.head + 1 == self.size:
            return True
        else:
            return False

    def Empty(self):
        if self.tail == self.head:
            return True
        else:
            return False


q = Queue(10)
q.Empty()
q.enQueue("Hello")
q.outQueue()
q.Full()
print(q)