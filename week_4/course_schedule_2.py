class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # use to keep tracking which node is being travesed
        stack = []
        adjacency_list = {i:[] for i in range(numCourses)}
        for [crs, pre] in prerequisites:
            adjacency_list[crs].append(pre)
        visited = set()

        def dfs(course):
            if course in visited:
                return False 
            if adjacency_list[course] == []:
                if course not in stack:
                    stack.append(course)
                return True 
            visited.add(course)

            for pre in adjacency_list[course]:
                if dfs(pre) == False:
                    return False
                
            visited.remove(course)
            if course not in stack:
                stack.append(course)
            # it worked, mark
            adjacency_list[course] = []
            return True

        for i in range(numCourses):
            if dfs(i)==False:
                return []
            
        return stack