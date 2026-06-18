class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        1 2 3 4 5. gas
        3 4 5 1 2. cost
              i

        tank = 0
        """
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        tank = 0
        for i in range(len(gas)):
            tank += gas[i]
            if tank < cost[i]:
                start = i + 1
                tank = 0
            else:
                tank -= cost[i]
        
        return start