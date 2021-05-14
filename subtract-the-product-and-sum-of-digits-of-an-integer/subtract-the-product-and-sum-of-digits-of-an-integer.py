class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum1 = 0
        for i in str(n):
            product = product * int(i)
            sum1 += int(i)

        return product-sum1
            
        