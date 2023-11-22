class DisjointSet:
    parent = {}

    def makeSet(self, items):
        for i in items:
            self.parent[i] = i

    def find(self, k):
        
        if self.parent[k] == k:
            return k
        
        return self.find(self.parent[k])
    
    def union(self, a, b):

        x = self.find(a)
        y = self.find(b)

        self.parent[x] = y

def print_sets(items, ds):
    print([ds.find(i) for i in items])    

if __name__ == '__main__':

    items = [1, 2, 3, 4, 5]

    ds = DisjointSet()

    ds.makeSet(items)
    print_sets(items, ds)

    ds.union(3,4)
    print_sets(items, ds)

    ds.union(1,2)
    print_sets(items, ds)

    ds.union(4,5)
    print_sets(items, ds)

    ds.union(1,5)
    print_sets(items, ds)