class KDTree():
    def __init__(self, P, d=0):
        n = len(P)
        m = n // 2  # median value
        P.sort(key = lambda x: x[d])
        self.point = P[m]
        d = (d+1)%len(P[0])
        if m > 0:
            self.left = KDTree(P[:m], d)
        elif n-(m+1)>=0:
            self.right = KDTree(P[m+1:], d)
         
