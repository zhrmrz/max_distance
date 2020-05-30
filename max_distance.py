class Sol:
    def max_distance(self,lol):
        high=lol[0][-1]
        low=lol[0][0]
        for list in lol[1:]:
            if min(list)<low:
                low=min(list)
            elif max(list)>high:
                high=max(list)
        return abs(high-low)

if __name__ == '__main__':
    p=Sol()
    print(p.max_distance([[1,2,3],
 [4,5],
 [1,2,3]]))
