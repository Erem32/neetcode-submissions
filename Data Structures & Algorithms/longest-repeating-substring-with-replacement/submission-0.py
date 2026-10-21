class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        res = 0
        maxf= 0
        for r in range(len(s)):
            #Loop counting the appearences of diffrent letters
            count[s[r]] = count.get(s[r],0) + 1
            maxf= max(maxf,count[s[r]])

            #check if we have the amount of replacements needed to make the entire string the same char
            while (r-l+1) - maxf > k:
                count[s[l]]-=1
                l+=1

            res = max(res,r-l+1)
        return res
