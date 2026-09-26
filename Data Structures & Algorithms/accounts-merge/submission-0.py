class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        # If x hasn't been seen, it's its own parent (its own group leader)
        if x not in self.parent:
            self.parent[x] = x
        # Follow the chain up to the root, compressing the path as we go
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x 


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        email_to_name = {}

    # Step 1 & 2: union emails within each account
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                email_to_name[email] = name
                uf.union(first_email, email)  # tie every email to the first one

        # Step 3: group emails by their root parent
        groups = defaultdict(list)
        for email in email_to_name:
            root = uf.find(email)
            groups[root].append(email)

        # Step 4: build the final merged list
        result = []
        for emails in groups.values():
            name = email_to_name[emails[0]]
            result.append([name] + sorted(emails))

        return result
        

'''
If an email in an incoming account already exists as a key in parent, then unioning it will attach the entire current account to whatever tree that email already belongs to — because first_email and that repeated email get merged into one group, dragging every other email in this account along with them.

Parent tracks if two emails are the same person, the emails trace back to a root - they dont give you information about who the person is
parent = {
    smith: smith,
    ny:    smith,
    "00":  smith
}


'''