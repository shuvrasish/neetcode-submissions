class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        vis = set()

        def dfs(node: int):
            if node in vis:
                return
            
            vis.add(node)

            for nei in adj[node]:
                dfs(nei)

        numComponents = 0
        for node in range(n):
            if node not in vis:
                dfs(node)
                numComponents += 1
        
        return numComponents
        

