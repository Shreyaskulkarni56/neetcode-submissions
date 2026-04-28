class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        Count =[0]*26
        for i in range(len(s)):
            Count[ord(s[i])-ord('a')]+=1
            Count[ord(t[i])-ord('a')]-=1
        for val in Count:
            if val != 0:
                return False
        return True