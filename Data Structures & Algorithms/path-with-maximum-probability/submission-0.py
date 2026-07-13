class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        adj= collections.defaultdict(list)

        for i in range(len(edges)):
            s, d = edges[i]
            w = succProb[i]
            adj[s].append((d,w))
            adj[d].append((s,w))

        probs = [0.0] * n
        probs[start_node] = 1.0

        maxHeap = [(-1.0, start_node)]

        while maxHeap:
            prob, n1 = heapq.heappop(maxHeap)
            prob = -prob

            if n1 == end_node:
                return prob
            
            if prob < probs[n1]:
                continue

            for n2, w2 in adj[n1]:
                if probs[n1] * w2 > probs[n2]:
                    probs[n2] = probs[n1] * w2
                    heapq.heappush(maxHeap, (-probs[n2], n2))
        
        return 0.0