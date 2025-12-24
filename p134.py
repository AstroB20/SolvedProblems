class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_gas = 0
        current_gas = 0
        start = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_gas += diff
            current_gas += diff
            if current_gas < 0:
                start = i + 1
                current_gas = 0
        return start if total_gas >= 0 else -1
