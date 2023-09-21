class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = []
        if x==0:
            return True
        while x > 0:
            temp.append(x%10)
            x=int(x/10)
        print(temp)
        for index, i in enumerate(temp):
            if temp[index] != temp[(len(temp)-index-1)] :
                return False

            print(temp[index], temp[(len(temp)-index-1)])


            if index+1 > int(len(temp) / 2):
                return True
            

run = Solution()
print(run.isPalindrome(8))

