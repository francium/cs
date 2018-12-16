class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return f'{self.value} -> {self.next_node}'


class LinkedList:
    def __init__(self, *values):
        self.head = Node(values[0])

        if len(values) == 1: return

        cur_node = self.head
        for v in values[1:]:
            cur_node.next_node = Node(v)
            cur_node = cur_node.next_node

    def append(self, value):
        cur_node = self.head
        while cur_node.next_node:
            cur_node = cur_node.next_node

        cur_node.next_node = Node(value)

    def get_last_node(self):
        cur_node = self.head
        while cur_node.next_node:
            cur_node = cur_node.next_node
        return cur_node


def reverse_linked_list(linked_list):
    print(linked_list.head)
    prev = None
    cur = linked_list.head
    nxt = cur.next_node
    while True:
        cur.next_node = prev
        prev = cur
        cur = nxt
        if not cur: break
        nxt = cur.next_node
    linked_list.head = prev


if __name__ == '__main__':
    l = LinkedList(1,2,3,4)
    l.append(9)
    print(l.head)
    print(l.get_last_node())
    reverse_linked_list(l)
    print(l.head)
