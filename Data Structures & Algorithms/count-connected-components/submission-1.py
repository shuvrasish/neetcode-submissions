class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, node):
        curr = node

        while curr != self.parent[curr]:
            self.parent[curr] = self.parent[self.parent[curr]]
            curr = self.parent[curr]
        
        return curr
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        if self.rank[pu] > self.rank[pv]:
            pu, pv = pv, pu
        
        self.parent[pu] = pv
        self.rank[pv] += self.rank[pu]
        return True



class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # adj = defaultdict(list)

        # for u, v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)

        # vis = set()

        # def dfs(node: int):
        #     if node in vis:
        #         return
            
        #     vis.add(node)

        #     for nei in adj[node]:
        #         dfs(nei)

        # numComponents = 0
        # for node in range(n):
        #     if node not in vis:
        #         dfs(node)
        #         numComponents += 1
        
        # return numComponents

        dsu = DSU(n)
        res = n

        for u, v in edges:
            if dsu.union(u, v):
                res -= 1
        
        return res
        

