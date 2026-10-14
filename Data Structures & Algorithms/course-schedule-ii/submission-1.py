class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = defaultdict(list)

        for course, pre in prerequisites:
            adj[course].append(pre)

        vis = [0] * numCourses
        
        res = []


        def dfs(crs: int) -> bool:
            if vis[crs] == 1:
                return False
            
            if vis[crs] == 2:
                return True
            
            vis[crs] = 1

            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            
            res.append(crs)
            vis[crs] = 2
            
            return True
        
        for crs in range(numCourses):
            if vis[crs] == 0:
                if not dfs(crs):
                    return []
                    
        return res