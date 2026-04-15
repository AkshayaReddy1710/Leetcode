class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        out=[0]*n
        revg=[[] for i in range(n)]
        for u in range(n):
            out[u]=len(graph[u])
            for v in graph[u]:
                revg[v].append(u)
        q=[]
        for i in range(n):
            if out[i]==0:
                q.append(i)
        safe=[False]*n
        while q:
            node=q.pop(0)
            safe[node]=True
            for prev in revg[node]:
                out[prev]-=1
                if out[prev]==0:
                    q.append(prev)
        res=[]
        for i in range(n):
            if safe[i]:
                res.append(i)
        return res
