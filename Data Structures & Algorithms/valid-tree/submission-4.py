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

        if not dfs(0, -1):
            return False

        return len(vis) == n
        

        