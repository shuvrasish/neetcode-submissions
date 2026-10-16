class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)

        vis = [0] * n

        def dfs(node: int, par: int):
            if vis[node] == 1:
                return False
            
            vis[node] = 1

            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            
            return True

        dfsCallCount = 0
        for node in range(n):
            if vis[node] == 0:
                dfsCallCount += 1
                if dfsCallCount > 1:
                    return False
                if not dfs(node, -1):
                    return False

        return True
        

        