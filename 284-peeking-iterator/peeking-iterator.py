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
PItr = []Itr

[[[1, 2, 3]]] -> hasnext, next
            i
nextInt = Itr.next = 2

"""

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.itr = iterator
        self.next_int = self.itr.next()
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.next_int
        

    def next(self):
        """
        :rtype: int
        """
        val = self.next_int
        if self.itr.hasNext():
            self.next_int = self.itr.next()
        else:
            self.next_int = None
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.next_int is not None

        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].