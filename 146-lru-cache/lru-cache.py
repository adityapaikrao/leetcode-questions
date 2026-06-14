"""
size -> capacity of cache

get(key) -> val of key else -1
put(key, value) -> puts into cache & updates & evict LRU


Cache 1:1, 2:2 3:3

map [key] -> value

- need some way to order by recent use
    de-queue? [1, 2, 4, 3] -> O(1) insert
                        O(1) pop front
            - but cant access middle element efficiently
            - use map to store location of key in store & this store should support O(1) removal
            - Linked List
              h -> 1 -> 2 -> 4 -> 3
              - need to access previosu element too => deque
              h <> 1 <> 4 <> 3 <> 2 <> t
              - when removing LRU its key has to be deleted in map as well
- 
"""
class Node:

    def __init__(self, key: int = None, val: int = None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self._hmap = {} # key -> Node
        self.size = capacity

        # Intialise linked list head & tails
        self._head = Node()
        self._tail = Node()

        self._head.next = self._tail
        self._tail.prev = self._head

    def _pop_node(self, node: Node) -> Node:
        # remove from LL 
        node.prev.next = node.next
        node.next.prev = node.prev

        return node

    def _move_to_back(self, node: Node):
        self._pop_node(node)
        self._add_to_back(node)
        
    def _add_to_back(self, node: Node):
        node.prev = self._tail.prev
        node.next = self._tail

        self._tail.prev.next = node
        self._tail.prev = node
    

    def get(self, key: int) -> int:
        if key not in self._hmap:
            return -1
        # make this key MRU
        self._move_to_back(self._hmap[key])

        return self._hmap[key].val

    def put(self, key: int, value: int) -> None:
        if key not in self._hmap:
            self._hmap[key] = Node(key, value)
            self._add_to_back(self._hmap[key])
        else:
            self._hmap[key].val = value

        self._move_to_back(self._hmap[key])
        if len(self._hmap) > self.size:
            removed = self._pop_node(self._head.next)
            del self._hmap[removed.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)