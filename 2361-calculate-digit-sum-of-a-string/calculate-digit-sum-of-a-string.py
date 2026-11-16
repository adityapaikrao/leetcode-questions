class Solution:
    def digitSum(self, s: str, k: int) -> str:
        curr = list(s)

        while len(curr) > k:
            new = []
            for i in range(0, len(curr), k):
                curr_sum = 0
                for j in range(i, min(i + k, len(curr))):
                    curr_sum += int(curr[j])
                new.extend([ch for ch in str(curr_sum)])
            curr = new
        return ''.join(curr)
