class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n: int = len(s)
        ones: int = 0
        zeros: int = 0
        for ch in s:
            if ch == '1': ones += 1
            else: zeros += 1
        if ones == n: return 0
        for i in range(1, n + 1):
            flips: int = k * i
            if (flips < zeros) or ((flips - zeros) & 1): continue
            elif i & 1:
                if zeros <= flips <= zeros * i + ones * (i - 1): return i
            elif zeros <= flips <= zeros * (i - 1) + ones * i: return i
        return -1
        