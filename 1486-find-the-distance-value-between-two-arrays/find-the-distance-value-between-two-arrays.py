class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0
        for num in arr1:
            if all(abs(num2 - num) > d for num2 in arr2):
                count += 1
        return count