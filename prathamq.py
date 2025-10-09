import math

class UserMainCode(object):
    @classmethod
    def solveEquation(cls, input1):
        N = input1
        if N < 6:
            return 0

        max_val = int(math.sqrt(N))
        count = 0

        for a in range(1, max_val + 1):
            if a*a + 2*a + 3 > N:
                break
            for b in range(1, max_val + 1):
                if a*a + b*b + a*b + a + b + 1 > N:
                    break
                for c in range(1, max_val + 1):
                    result = (a*a) + (b*b) + (c*c) + (a*b) + (b*c) + (c*a)
                    if result == N:
                        count += 1
                    if result > N:
                        break
        return count
print(UserMainCode.solveEquation(11
                                 ))  # Example usage