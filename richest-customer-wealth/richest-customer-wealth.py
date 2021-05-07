class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxwealth = 0
        for i in accounts:
            total = 0
            for j in range (len(i)):
                total += i[j]
            
            
            if total > maxwealth:
                maxwealth = total
        return maxwealth