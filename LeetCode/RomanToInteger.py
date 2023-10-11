
class Solution:
    roman = ["I", "V", "X", "L", "C", "D", "M"]
    value = [1, 5, 10, 50, 100, 500, 1000]
    def romanToInt(self, s: str) -> int:
        temp = self.splitRoman(s).copy()
        result = 0
        for index, i in enumerate(temp):
            if index > 0 and temp[index-1]=="I" and (temp[index]=="V" or temp[index]=="X"):
                result-=2
            if index > 0 and  temp[index-1]=="X" and (temp[index]=="L" or temp[index]=="C"):
                result-=20
            if index > 0 and  temp[index-1]=="C" and (temp[index]=="D" or temp[index]=="M"):
                result-=200
            result += self.translate(i)
        return result


    def splitRoman(self, s:str):
        temp = []
        for i in s:
            temp.append(i)
        return temp

    def translate(self, s) -> int:
        for index, v in enumerate(self.roman):
            if s==v:
                return self.value[index]
        return 0
run = Solution()
print(run.romanToInt("MMMCDXC"))


































































































































