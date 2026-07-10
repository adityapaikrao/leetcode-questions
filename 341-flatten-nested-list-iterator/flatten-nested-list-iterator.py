# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
"""
[1, [2, 3], [[4]], [[]]]
     i
 1
recurse on [2, 3] 
"""

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flattened = deque()
        def flatten(nested_list: [NestedInteger]):
            for nested_int in nested_list:
                if nested_int.isInteger():
                    self.flattened.append(nested_int.getInteger())
                else:
                    flatten(nested_int.getList())
        flatten(nestedList)

    def next(self) -> int:
        return self.flattened.popleft()
    
    def hasNext(self) -> bool:
         return len(self.flattened) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())