class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcandy = max(candies)
        print(maxcandy)
        newlist = []
        for i in candies:
            
            if (i + extraCandies >= maxcandy) == True:
                newlist.append(True)
            else:
                newlist.append(False)
                
        return newlist
        