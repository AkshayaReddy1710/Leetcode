class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        def backtrack():
            if len(path) == len(nums):
                result.append(path[:])
                return
            for value in nums:
                if value not in path:
                    path.append(value)
                    backtrack()
                    path.pop()
        backtrack()
        return result
        