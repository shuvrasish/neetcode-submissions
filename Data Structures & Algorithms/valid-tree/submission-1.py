class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)

        vis = set()

        def dfs(node: int, par: int):
            if node in vis:
                return False
            
            vis.add(node)

            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            
            return True

        dfsCallCount = 0
        for node in range(n):
            if node not in vis:
                dfsCallCount += 1
                if dfsCallCount > 1:
                    return False
                if not dfs(node, -1):
                    return False

        return True
        

        