class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        m1=0
        chset=set()
        for r in range(len(s)):
            if s[r] not in chset:
                chset.add(s[r])
                m1=max(m1,r-left+1)
            else:
                while s[r] in chset:
                    chset.remove(s[left])
                    left+=1
                chset.add(s[r])
        return m1        