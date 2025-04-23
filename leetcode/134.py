# 134. Gas Station
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = sum(gas)
        total_cost = sum(cost)

        if total_gas < total_cost:
            return -1

        start = 0
        tank = 0
        for i in range(len(gas)):
            tank += gas[i]
            if tank >= cost[i]:
                # can continue to the next station
                tank -= cost[i]
            else:
                # restart at the next station that can not be reached
                tank = 0
                start = i+1
        return start
