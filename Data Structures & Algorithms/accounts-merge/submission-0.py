class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        #each element is a list of strings 
        # accounts[i][0]= name and then every other index= email

        # basically if accounts[i][0] = the same across different indexes in accounts and they share the same email, then append

        adj = defaultdict(list)

        for account in accounts:
            for email in account[2:]:
                adj[email].append(account[1])
                adj[account[1]].append(email)

        visit = set()
        res = []

        for account in accounts:
            name = account[0]
            start = account[1]

            if start in visit:
                continue

            q = deque([start])
            visit.add(start)
            emails = []

            while q:
                email = q.popleft()
                emails.append(email)

                for nei in adj[email]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)
            res.append([name] + sorted(emails))
        return res