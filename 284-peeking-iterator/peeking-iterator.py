# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """
"""
  1 2 3
i
  n

next -> 1 
  1 2 3
i
    n
  c

peek -> 2
  1 2 3
i
    n
  c
next -> 2
  1 2 3
i
      n
next -> 3
  1 2 3
i
      n
"""



class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.itr = iterator
        self.next_elem = self.itr.next() if self.itr.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.next_elem
        

    def next(self):
        """
        :rtype: int
        """
        curr_next = self.next_elem
        self.next_elem = self.itr.next() if self.itr.hasNext() else None

        return curr_next
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.next_elem is not None
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].