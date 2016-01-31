class HT(object):
    def __init__(self,size):
        self.pegA = []
        for i in range(size,0,-1):
            self.pegA.append(i)
        self.pegB = []
        self.pegC = []

    def __str__(self):
        return str(self.pegA) + ' ' + str(self.pegB) + ' ' +str(self.pegC)


    def get(self,i):
        if i == 0:
            return self.pegA
        if i == 1:
            return self.pegB
        if i == 2:
            return self.pegC
    
    def move(self,pegs,pegd):
        try:
            self.get(pegd).append(self.get(pegs).pop())
        except IndexError as e:
            pass

    def height(self,peg):
        return len(self.get(peg))


def solve(size):
    h = HT(size)
    print(h)
    def moveStack(n,source,destination,mid):
        print(h)
        if(n == 0):
            h.move(source,destination)
        else:
            moveStack(n-1,source,mid,destination)
            h.move(source,destination)
            moveStack(n-1,mid,destination,source)
    moveStack(size,0,2,1)
    print(h)

solve(10)
