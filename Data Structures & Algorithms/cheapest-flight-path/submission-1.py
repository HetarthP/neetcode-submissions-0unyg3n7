class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        #from, to , money for flights[i] 

        #src= starting, dst= destination airport, k= max stops 
        #return cheapest price from src to dst with <=k stops or -1 

        #dijkstras using min heap for this 


        #this makes the adj list 
        adj=[[] for _ in range(n)]

        for start, fin, price in flights:
            adj[start].append((fin, price))


        cheapest={} 

        #for flights/stops used too- src is where we start from 
        minHeap= [(0,src,0)]

        while minHeap: 

            cost, node, flights_used= heapq.heappop(minHeap)

            if node== dst:
                return cost 
            if flights_used > k:
                continue 

            if node in cheapest and cheapest[node] <= flights_used:
                continue 
            cheapest[node]= flights_used  

            for nei,price in adj[node]: 
                    heapq.heappush(minHeap, (cost+price, nei, flights_used+1))
        return -1