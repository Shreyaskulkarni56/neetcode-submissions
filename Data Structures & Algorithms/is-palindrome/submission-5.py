class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while r>l:
            if s[l]==s[r]:
                return True
            l+=1
            r-=1
        return False