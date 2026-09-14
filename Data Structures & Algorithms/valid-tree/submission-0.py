class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        

        if len(edges)!= n-1:
            return False 

         
        graph= [[] for _ in range(n)]

        for a,b in edges:

            graph[a].append(b)
            graph[b].append(a) 

        
        q= deque([0])
        seen= {0}

        while q: 

            node= q.popleft() 

            for nei in graph[node]:

                if nei not in seen:
                    seen.add(nei)
                    q.append(nei)

        return len(seen)==n