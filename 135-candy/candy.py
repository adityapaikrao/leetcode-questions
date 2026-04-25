class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        1 2 3 1
        """
        num_candies = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                num_candies[i] = num_candies[i-1] + 1
        # print(num_candies)
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and num_candies[i] <= num_candies[i + 1]:
                num_candies[i] = num_candies[i + 1] + 1
        
        return sum(num_candies)