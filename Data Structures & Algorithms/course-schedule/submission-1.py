class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for crs, pre in prerequisites:
            adj[crs].append(pre) # a depends on b, 0 depends on 1 for [0, 1]
        
        vis = defaultdict(int)
        def dfs(crs: int) -> bool: # True -> possible
            if crs in vis:
                if vis[crs] == 2: # completed
                    return True 
                if vis[crs] == 1: # cycle
                    return False 

            vis[crs] = 1
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            
            vis[crs] = 2
            return True

        for course in range(numCourses):
            if course not in vis:
                if not dfs(course):
                    return False


        return True
