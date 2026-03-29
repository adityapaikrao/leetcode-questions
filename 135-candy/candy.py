class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        num_candies = candies[-1]
        for i in range(len(candies) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                if candies[i + 1] + 1 > candies[i]:
                    candies[i] = candies[i + 1] + 1
            num_candies += candies[i]
        
        return num_candies