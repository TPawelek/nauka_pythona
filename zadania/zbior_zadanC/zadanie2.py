import math


class Calculate:
    def pow(self, x, n):
        x = x
        n = n
        count = math.pow(x, n)
        return count


one = Calculate()
print(one.pow(5, 2))
