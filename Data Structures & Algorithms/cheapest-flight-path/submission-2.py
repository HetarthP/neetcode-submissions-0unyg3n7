class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj=[[] for _ in range(n)]

        for start, end, price in flights:

            adj[start].append((end,price))

        
        cheapest={} 

        minHeap= [(0,src,0)]

        while minHeap:

            cost, node, flights_used= heapq.heappop(minHeap)
            
            if node==dst:
                return cost

            if flights_used >k:
                continue 

            if node in cheapest and cheapest[node] <= flights_used:
                continue
            cheapest[node]= flights_used 

            for neigh, price in adj[node]:

                heapq.heappush(minHeap, (cost+price, neigh, flights_used+1))

        return -1 
                

             
        