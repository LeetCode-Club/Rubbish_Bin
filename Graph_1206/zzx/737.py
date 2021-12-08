class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        parent = {}
        
        def find(p):
            if p not in parent:
                parent[p] = p
            while p != parent[p]:
                p = parent[p]
            return p    
        
        def union(p, q):
            i = find(p)        
            j = find(q)
            if i != j:
                parent[i] = j
                
        for p, q in pairs:
            union(p, q)
            
        return all(find(a) == find(b) for a, b in zip_longest(words1, words2))
        