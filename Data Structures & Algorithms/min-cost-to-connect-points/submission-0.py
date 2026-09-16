class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n= len(points)

        adj= {i:[] for i in range(n)}

        for i in range(n):

            x1,y1= points[i]

            for j in range(i+1,n):

                x2,y2= points[j]

                cost= abs(x1-x2) + abs(y1-y2)


                adj[i].append((cost,j))
                adj[j].append((cost,i))


        minHeap=[(0,0)]
        visited= set()
        res=0 

        while len(visited)<n:

            cost, node= heapq.heappop(minHeap) 


            if node in visited:
                continue 
            visited.add(node) 

            res+= cost 

            for weight, nei in adj[node]:
                if nei not in visited:

                    heapq.heappush(minHeap, (weight,nei))
        return res