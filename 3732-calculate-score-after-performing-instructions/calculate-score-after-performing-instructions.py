class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        score = 0
        seen = set()
        i = 0

        while True:
            if i in seen or i < 0 or i >= len(instructions):
                break
            seen.add(i)
            if instructions[i] == "jump":
                i += values[i]
            else:
                score += values[i]
                i += 1
        
        return score

