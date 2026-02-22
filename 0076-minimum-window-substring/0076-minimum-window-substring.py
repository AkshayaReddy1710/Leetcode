class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        n=len(s)
        freq={}
        for c in t:
            if c in freq:
                freq[c]+=1
            else:
                freq[c]=1
        left=0
        c=0
        start=0
        m1=float('inf')
        for r in range(n):
            if s[r] in freq:
                if freq[s[r]]>0:
                    c+=1
                freq[s[r]]-=1
            else:
                freq[s[r]]=-1
            while c==len(t):
                if r-left+1<m1:
                    m1=r-left+1
                    start=left
                freq[s[left]]+=1
                if freq[s[left]]>0:
                    c-=1
                left+=1
        if m1==float('inf'):
            return ""
        else:
            return s[start:start+m1]
            


        