class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        n1 = len(num1)
        n2 = len(num2)
        result = [0] * (n1 + n2)
        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                iSum = mul + result[i + j + 1]
                result[i + j] += iSum // 10
                result[i + j + 1] = iSum % 10
        result = ''.join(map(str, result))
        return result.lstrip('0')