class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        oldrow = [1]
        finaloutputlist = []
        for i in range(rowIndex + 1): 
            finaloutputlist.append(oldrow.copy())
           
  
            oldrow.append(0)
            oldrow.insert(0,0)
  
            j = i + 1
            newrow = []
            for i in range(len(oldrow) -1):
                #print(oldrow[i])
                newrow.append(oldrow[i] + oldrow [i+1])
  
            oldrow = newrow

        return finaloutputlist[-1]
        