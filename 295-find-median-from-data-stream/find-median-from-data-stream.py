"""
num < 0 to 10^-5

stream = [2] 
[2] median = 2
[2, 3] median = 2.5
[2, 3, 4] median = 3

L R -> median average (max in L) & (min in R) if L + R is even o.w max in L [L > R + 1]
L: max_heap
R: min_heap

Invariant:
- every elem in L <= every elem in R
- len(L) - len(R) <= 1

Approach
- new num comes in
- push into L
- check invariant condiation:
    - if len(L) > len(R) + 1: pop from L put into R
    - if L >= R: swap elems
- median = [max(L) + min(R)] / 2 if len(L) + len(R) is even
- ow max(L)

6 2 1 8 9
[6] [] median: 6
[2] [6] : 4
[2, 1] [6] : 2
[2, 1] [6, 8] :3.5
[2, 1, 6] [9, 8] :5
-3, 2
[-1] [2]
"""


class MedianFinder:

    def __init__(self):
        self.heap_l = []
        self.heap_r = []

    def addNum(self, num: int) -> None:
        # push num into left heap - max_heap
        heapq.heappush(self.heap_l, -num)

        # check constraints
        if len(self.heap_l) > len(self.heap_r) + 1:
            popped = -1 * heapq.heappop(self.heap_l)
            heapq.heappush(self.heap_r, popped)
        elif self.heap_r and (self.heap_l[0] * -1) > self.heap_r[0]:
            # swap elems
            popped_left, popped_right = heapq.heappop(self.heap_l), heapq.heappop(self.heap_r)

            # push into heaps
            heapq.heappush(self.heap_l, popped_right * -1)
            heapq.heappush(self.heap_r, popped_left * -1)

    def findMedian(self) -> float:
        # compute median
        median = 0
        if (len(self.heap_l) + len(self.heap_r)) % 2 == 0:
            median = ((self.heap_l[0] * -1) + self.heap_r[0]) / 2
        else:
            median = self.heap_l[0] * -1
        
        return median
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()