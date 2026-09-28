from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails = defaultdict(list)
        for i in range(len(accounts)):
            for x in range(1, len(accounts[i])):
                emails[accounts[i][x]].append(i) # email - accounts
        print(emails)
        visited = set()
        
        parent = {}
        rank = {}
        for i in range(0, len(accounts)):
            parent[i] = i
            rank[i] = 0

        def find (n):
            p = n
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]

            
            return p
        
        def merge(a,b):
            p1, p2 = find(a), find(b)
            if p1 == p2:
                return False
        
            if rank[p1] > rank[p2]:
                parent[p2] = p1
            elif rank[p1] < rank[p2]:
                parent[p1] = p2
            
            else:
                parent[p1] = p2
                rank[p1] += 1

        for acc in emails.values():
            for i in range(len(acc) - 1):
                merge(acc[i], acc[i+1])

        components = defaultdict(list)

        for email, indices in emails.items():
            #since indeices are already merged together
            print(indices[0])
            root = find(indices[0])
            components[root].append(email)
        
        res = []
        for indices, emails in components.items():
            #sort it and append parent
            emails = sorted(emails)
            name = accounts[indices][0]
            res.append([name] + emails)

        return res
