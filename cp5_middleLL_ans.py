class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertHead(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def append(self, x):
        if self.head is None:
            self.head = Node(x)
            return
        tmp = self.head
        while tmp.next is not None:
            tmp = tmp.next
        tmp.next = Node(x)

    def printLinkedList(self):
        tmp = self.head
        print("[", end="")
        while tmp is not None:
            print(tmp.data, end="")
            tmp = tmp.next
            if tmp is not None:
                print(", ", end="")
        print("]")

    def find_median(self):
        if not self.head:
            return None
        length = 0
        tmp = self.head
        while tmp:
            length += 1
            tmp = tmp.next
        if length % 2 == 1:
            middle_index = length // 2
            tmp = self.head
            for _ in range(middle_index):
                tmp = tmp.next
            return tmp.data
        else:
            middle_index = length // 2
            prev = None
            tmp = self.head
            for _ in range(middle_index):
                prev = tmp
                tmp = tmp.next
            return (prev.data + tmp.data) / 2

def main():
    ll = LinkedList()
    ll.insertHead(1)
    ll.append(2)
    ll.append(3)
    ll.append(3)
    ll.printLinkedList()
    print(ll.find_median())

if __name__ == "__main__":
    main()
