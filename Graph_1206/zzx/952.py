class UnionFind:
    def __init__(self, n: int):
        self.parent = [x for x in range(n)]
        self.size = [1 for _ in range(n)]
        self.part = n
    
    def Find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.Find(self.parent[x])
        return self.parent[x]
    
    def Union(self, x: int, y: int) -> bool:
        root_x = self.Find(x)
        root_y = self.Find(y)
        if root_x == root_y:
            return False
        if self.size[root_x] > self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_x] = root_y
        self.size[root_y] += self.size[root_x]
        self.part -= 1
        return True

    def get_part_size(self, x: int) -> int:
        root_x = self.Find(x)
        return self.size[root_x]

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = max(nums)
        UF = UnionFind(n + 1)
        for num in nums:
            for x in range(2, int(num ** 0.5) + 1):
                if num % x == 0:
                    UF.Union(num, num // x)
                    UF.Union(num, x)
        dic = defaultdict(int)
        for num in nums:
            dic[UF.Find(num)] += 1
        return max(dic.values())        #连接结点最多的那个因子， 的连接频率
