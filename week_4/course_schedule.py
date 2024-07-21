class Solution:
    def canFinish(self, numCourses, prerequisites):
        # if the adjacent list entry is empty means that we can complete this course as it has not dependence
        adjacent_map = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            adjacent_map[crs].append(pre)
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if adjacent_map[course] == []:
                return True
            visited.add(course)
            
            for pre in adjacent_map[course]:
                if dfs(pre) == False:
                    return False
            visited.remove(course)
            # this course can be completed, mark to save time
            adjacent_map[course] = []
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return False 
        return True

