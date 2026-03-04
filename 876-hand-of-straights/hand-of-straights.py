"""
1 2 2 3 3 4 6 7 8
    s     
    i

size: 3

1 2 3
"""

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        counts = defaultdict(int)
        for num in hand:
            counts[num] += 1
        
        hand.sort()
        
        for num in hand:
            if counts[num] == 0:
                continue
            
            curr = num
            curr_size = 1
            counts[curr] -= 1

            while counts[curr + 1] > 0 and curr_size < groupSize:
                curr_size += 1
                counts[curr + 1] -= 1
                curr += 1
            
            if curr_size < groupSize:
                return False
            

        return True
                