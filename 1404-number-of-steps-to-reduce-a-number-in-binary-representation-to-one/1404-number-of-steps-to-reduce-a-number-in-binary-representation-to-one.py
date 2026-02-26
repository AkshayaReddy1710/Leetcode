class Solution:
    def add_one(self, s):
        i = len(s) - 1
        while i >= 0 and s[i] == '1':
            s[i] = '0'
            i -= 1
        if i < 0:
            s.insert(0, '1')
        else:
            s[i] = '1'
    def divide_by_two(self, s):
        s.pop()
    def numSteps(self, s: str) -> int:
        s = list(s)
        operations = 0
        while len(s) > 1:
            if s[-1] == '0':
                self.divide_by_two(s)
            else:
                self.add_one(s)
            operations += 1
        return operations
