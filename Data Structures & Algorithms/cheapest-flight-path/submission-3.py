class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj= [[] for _ in range(n)]

        for start,fin, cost in flights:

            adj[start].append((fin, cost))

        
        cheapest= {} 

        minHeap= [(0,src,0)]

        while minHeap:

            price, node, flights_used = heapq.heappop(minHeap) 

            if node== dst:
                return price 

            if flights_used > k:
                continue 
            
            if node in cheapest and cheapest[node]<= flights_used:
                continue 
            cheapest[node] = flights_used

            for nei, cost in adj[node]:

                heapq.heappush(minHeap, (cost + price, nei, flights_used+1))

        return -1