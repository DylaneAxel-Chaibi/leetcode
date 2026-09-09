class ListNode:

    def __init__(self, key=-1, value=-1, next=None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for i in range(1000)]

    def put(self, key: int, value: int) -> None:
        index = key % 1000
        node = self.map[index]
        while node.next :
            if key == node.key :
                node.value = value
                return
            node = node.next
        if key == node.key :
            node.value = value
        else :
            node.next = ListNode(key, value, None)

    def get(self, key: int) -> int:
        index = key % 1000
        node = self.map[index]
        while node :
            if key == node.key :
                return node.value
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        index = key % 1000
        prev = node = self.map[index]
        while prev.next :
            node = prev.next
            if key == node.key :
                prev.next = node.next
                return
            prev = prev.next
        return 
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)