from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        arr2 = []
        length = 0
        for i in strs:
            if len(i) > length:
                length = len(i)     

        for h in strs:
            temp = []
            leng = length
            while leng > 0:
                leng -= 1
                if leng > len(h)-1:
                    temp.append(None)
                else:
                    temp.append(h[leng])
            arr2.append(temp)       
        
        
        leng = length
        arr3 = []
        index = 0
        while leng > 0:
            temp = []
            leng -= 1
            for h in arr2:
                temp.append(h[index])
            index += 1
            arr3.append(temp)

            
        return arr3[4] == arr3[5]
    

strs = ["flower","flow","flight"]
run = Solution()
print(run.longestCommonPrefix(strs))