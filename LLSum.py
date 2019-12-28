class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        new_node = Node(data)
        if (self.__head == None):
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def display(self):
        temp = self.__head
        while (temp is not None):
            print(temp.get_data())
            temp = temp.get_next()

    def maxVal(self):
        temp = self.__head
        l = temp.get_data()
        while(temp is not None):
            if (temp.get_data() > l):
                l = temp.get_data()
            temp = temp.get_next()
        print("Largest: ", l)

        temp1 = self.__head
        while(temp1 is not None):
            if(temp1.get_data() == l):
                temp1.set_data(10)
            temp1 = temp1.get_next()


numList = LinkedList()
numList.add(1)
numList.add(2)
numList.add(4)
numList.add(3)

numList.maxVal()
numList.display()