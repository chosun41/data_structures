import collections

def findOrder(numCourses, prerequisites):
    print(prerequisites)
    graph = collections.defaultdict(set)
    neighbors = collections.defaultdict(set)
    for course, pre in prerequisites:
        graph[course].add(pre) # to, from
        neighbors[pre].add(course) # from, to

    print(graph)
    print(neighbors)

    stack = [n for n in range(numCourses) if not graph[n]] #anything without an indegree
    print(stack)

    result = []
    while stack:
        node = stack.pop()
        result.append(node) # add node to stack
        if node in neighbors:
            for n in neighbors[node]:
                graph[n].remove(node) 
                if not graph[n]:
                    stack.append(n) # only add to stack if no indegree anymore

    return result if len(result) == numCourses else []


if __name__ == '__main__':
    
    # There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    # For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
    # Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

    

    # Example 1:

    # Input: numCourses = 2, prerequisites = [[1,0]]
    # Output: [0,1]
    # Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
    # Example 2:

    # Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    # Output: [0,2,1,3]
    # Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
    # So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
    # Example 3:

    # Input: numCourses = 1, prerequisites = []
    # Output: [0]
    

    # Constraints:

    # 1 <= numCourses <= 2000
    # 0 <= prerequisites.length <= numCourses * (numCourses - 1)
    # prerequisites[i].length == 2
    # 0 <= ai, bi < numCourses
    # ai != bi
    # All the pairs [ai, bi] are distinct.

    print(findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))

    # stack = [0]
    # stack = [] node=0
    # result = [0]
    # 0: {1, 2}
    # graph = {1: {}, 2: {0}, 3: {1, 2}} stack = [1], graph = {1: {}, 2: {}, 3: {1, 2}} stack = [1,2]

    # stack =[1] node=2
    # result = [0,2]
    # 2: {3}
    # graph = {1: {}, 2: {}, 3: {1}}

    # stack = [] node = 1
    # result = [0,2,1]
    # 1: {3}
    # graph = {1: {}, 2: {}, 3: {}} stack =[3]

    # stack = [] node = 3
    # result = [0,2,1,3]

    print(findOrder(numCourses = 1, prerequisites=[]))