class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        oldrow = [1]
        finaloutputlist = []
        for i in range(numRows): 
          finaloutputlist.append(oldrow.copy())
          

          oldrow.append(0)
          oldrow.insert(0,0)

          j = i + 1
          newrow = []
          for i in range(len(oldrow) -1):
           
            newrow.append(oldrow[i] + oldrow [i+1])

          oldrow = newrow

        return finaloutputlist