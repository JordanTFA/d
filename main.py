from random import choice ,randint, shuffle

def makemaze(width, height):

    visited = []
    popped = []
    result = []
    print("D: [0,0]\n")

    def walk(x,y):

        outOfBounds = []
        v = []
        visited.append([x,y])

        north = [x, y - 1]
        east = [x + 1, y]
        south = [x, y + 1]
        west = [x - 1, y]

        directions = [north, east, south, west]

        for index in range(3,-1,-1):
            xx,yy = directions[index]
            if xx < 0 or xx >= width or yy < 0 or yy >= height:
                del directions[index]
                outOfBounds.append([xx,yy])

            if [xx,yy] in visited or [xx,yy] in popped:
                v.append([xx,yy])
                if directions:
                    del directions[index]

        # Valid tile - let's continue
        if directions:
            d = choice(directions)
            result.append(str(visited[-1]) + " <-> " + str(d))

            print("Out of Bounds: ", outOfBounds)
            print("Visited tiles: ", v)
            print("Available directions : ", directions)
            print("D: ", d)
            print("Result: ", result[-1])
            print()

            if (len(visited) + len(popped)) < ((height * width) - 1):
                walk(d[0], d[1])

        # No neighbours - time to backtrack...
        else:
            print("No Neighbours")
            print("Visited: ", visited)
            print("Popped: ", popped)
            popped.append(visited[-1])
            visited.pop()
            d = visited[-1]
            visited.pop()
            print("D: ", d)
            print()

            walk(d[0], d[1])
    walk(0,0)

    for r in result:
        print(r)
    
def drawmaze(width, height):
    
    hw = "|  "
    hp = "   "
    
    vw = "+--"
    vp = "+  "
    
    row = ""

    print()
    #grid[width][height] 
    #horz = ["|  |           |", "|     |     |  |", "|  |  |     |  |", "|        |  |  |", "|        |  |  |"]
    #vert = ["+  +  +--+  +  +", "+--+  +--+--+  +", "+  +  +  +  +  +"]
    row += hw + hw + hp + hp + hp + hw
    row += vp + vp + vw + vp + vp + vw
    print(row)

    #print(("+--" * width) + "+")
    #for i in range(height):
        #print (horz[i])
        #if i < len(vert):
            #print(vert[i])
    #for i in range(height):
        #print(("+--" * width) + "+")
        #print("|  " * (width + 1))

    #Print floor
    print(("+--" * width) + "+")

    print()
    print("+--+--+--+--+--+")
    print("|  |           |")
    print("+  +  +--+  +  +")
    print("|     |     |  |")
    print("+--+  +--+--+  +")
    print("|  |  |     |  |")
    print("+  +  +  +  +  +")
    print("|        |  |  |")
    print("+--+--+--+--+--+")
if __name__ == '__main__':

    width, height = 5,4
    makemaze(width, height)
    drawmaze(width, height)
