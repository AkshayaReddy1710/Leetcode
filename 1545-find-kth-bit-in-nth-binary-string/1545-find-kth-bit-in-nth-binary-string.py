class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s="0"
        for i in range(2,n+1):
            inverted=""
            for ch in s:
                if ch=="0":
                    inverted+="1"
                else:
                    inverted+="0"
            inverted=inverted[::-1]
            s=s+"1"+inverted
        return s[k-1]