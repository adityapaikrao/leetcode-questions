class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        1 3 5 7 2 1 1 4
          
        - - p p p d d d d d - - 
                          i
        1 1 2 3 4 1 2 3 4 5
        """
        num_candies = 1
        i = 1

        while i < len(ratings):
            while i < len(ratings) and ratings[i] == ratings[i-1]:
                i += 1
                num_candies += 1
            
            peak = 1
            while i < len(ratings) and ratings[i] > ratings[i-1]:
                peak += 1
                num_candies += peak
                i += 1
            
            valley = 0
            while i < len(ratings) and ratings[i] < ratings[i-1]:
                valley += 1
                num_candies += valley
                i += 1

            if valley + 1 > peak:
                num_candies += valley + 1 - peak
            
        
        return num_candies
        

