class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        else:
            final = ""
            flipper = 1
            x = 0
            mylist = []
            mydict = {}
            for j in range(numRows):
                mydict[j + 1] = list()
            for i in range(len(s)):
                mylist.append(s[i])
            while mylist != []:
                if x == 1:
                    flipper = 1
                if x == numRows:
                    flipper = -1
                x = x + flipper

                mydict[x].extend(mylist[0])
                del mylist[0]
            for key, value in mydict.items():
                final += "".join(value)


            return final
            
            
