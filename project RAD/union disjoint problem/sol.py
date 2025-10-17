from typing import List
class UnionFind:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[0]*n
        self.count=n
    def find(self ,i):
        if self.parent[i]!=i:
            self.parent[i]=self.find(self.parent[i])
        return self.parent[i]
    def union(self,i,j):
        root_i=self.find(i)
        root_j=self.find(j)
        if root_i!= root_j:
            if self.rank[root_i]<self.rank[root_j]:
                self.parent[root_i]=root_j
            elif self.rank[root_i]>self.rank[root_j]:
                self.parent[root_j]=root_i
            else:
                self.parent[root_j]=root_i
                self.rank[root_i]+=1
            self.count-=1
            return True
        return False
def countComponents(n:int,edges:List[List[int]])-> int:
        uf=UnionFind(n)
        for u,v in edges:
            uf.union(u,v)
        return uf.count
        

if __name__ == "__main__":
    test_cases = [
        (5, [[0, 1], [1, 2], [3, 4]], 2),
        (5, [[0, 1], [1, 2], [2, 3], [3, 4]], 1),
        (4, [[0, 1], [2, 3]], 2),
        (6, [[0, 1], [2, 3], [4, 5], [0, 5]], 2), # [[0,1,5,4], [2,3]]
        (3, [], 3)
    ]

    print("--- Number of Connected Components (Union-Find) Test Results ---")
    
    for n, edges, expected in test_cases:
        result = countComponents(n, edges)
        status = "PASSED" if result == expected else f"FAILED (Expected: {expected}, Got: {result})"
        
        print(f"Nodes: {n}, Edges: {edges} -> Components: {result}, Status: {status}\n")