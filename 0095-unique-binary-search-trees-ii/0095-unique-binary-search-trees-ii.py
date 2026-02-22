class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def build(l, r):
            if l > r:
                return [None]
            res = []
            for i in range(l, r + 1):
                for left in build(l, i - 1):
                    for right in build(i + 1, r):
                        node = TreeNode(i)
                        node.left = left
                        node.right = right
                        res.append(node)
            return res
        return build(1, n)