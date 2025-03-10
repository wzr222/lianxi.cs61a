def pair(x, y):
        """Return a function that represents a pair."""
        def get(index):
            if index == 0:
                return x
            elif index == 1:
                return y
        return get
def select(p, i):
        """Return the element at index i of pair p."""
        return p(i)
p = pair(20, 14)
select(p, 0)
select(p,1)