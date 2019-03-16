import math

class Portal:

    def __init__(self, xin, yin, xout, yout):
        self.xin = int(xin)
        self.yin = int(yin)
        self.xout = int(xout)
        self.yout = int(yout)

    def dist(self, x, y):
        return abs(self.xin - x) + abs(self.yin - y)



def start():
    text = ""
    t = int(input())

    if (t < 1 or t > 20):
        return

    for i in range(t):
        size = input().split(" ")
        size[0] = int(size[0])
        size[1] = int(size[1])
        
        if (size[0] < 1 or size[0] > 100000 or size[1] < 1 or size[1] > 100000):
            continue
        
        start = input().split(" ")
        start[0] = int(start[0])
        start[1] = int(start[1])

        if (start[0] < 0 or start[0] >= size[0] or start[1] < 0 or start[1] >= size[1]):
            continue
        
        y = int(input())

        if (y < 2 or y > 2000):
            continue
        
        portals = []
        for x in range(y):
            xin, yin, xout, yout = input().split(" ")
            xin = int(xin)
            yin = int(yin)
            xout = int(xout)
            yout = int(yout)

            if (xin < 0 or xin >= size[0] or yin < 0 or yin >= size[1]):
                continue
            
            portals.append(Portal(xin, yin, xout, yout))

        x = int(start[0])
        y = int(start[1])
        d = 0
        while (len(portals) > 0):
            _min = 1000000000000000000000
            current = None
            for portal in portals:
                if (portal.dist(x, y) == _min):
                    if (portal.xin == current.xin):
                        if (portal.yin < current.yin):
                            current = portal
                    elif (portal.xin < current.xin):
                        current = portal
                elif (portal.dist(x, y) < _min):
                    current = portal
                    _min = portal.dist(x, y)

            d += abs(x - current.xin) + abs(y - current.yin)
            
            x = current.xout
            y = current.yout

            del portals[portals.index(current)]

        text += "Case #%s: %s" %(i + 1, d % 100003) + "\n"

    with open("text.txt", "w") as file:
        file.write(text)

start()
