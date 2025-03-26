from GetConnections import GetConnections

class PathPlan:
    def __init__(self,filename):
        connections = GetConnections(filename)
        self.nodes,_ = connections.getConnections()
        # print(self.nodes)

    def getPath(self,node1,node2,possPaths=[]):
        startIndices = []
        endIndices = []

        i = 0
        for location in self.nodes[0]:
            if location == node1:
                startIndices.append(i)
            i += 1

        i = 0
        for location in self.nodes[2]:
            if location == node2:
                endIndices.append(i)
            i += 1

        # This is all gross and wrong
               
        for startIndex in startIndices:
            path = [] 
            path.append(startIndex)
            nextIndices = self.getNext(startIndex)
            end = False
            while not end:
                for index in nextIndices:
                    path.append(index)
                    if index in endIndices:
                        end = True
                        possPaths.append(path)
                        print(path)
                    else:
                        nextIndices = self.getNext(index)

        return possPaths
        

    def getNext(self,index,nextIndices=[]):
        nextLoc = self.nodes[2][index]
        i = 0
        for location in self.nodes[0]:
            if location == nextLoc:
                nextIndices.append(i)
            i += 1
        return nextIndices




def main(args=None):
    userFile = input("What file: ")
    planner = PathPlan(userFile)
    # node1 = input("Node 1: ")
    # node2 = input("Node 2: ")
    node1 = "Tutorial_01"
    node2 = "Crossroads_16"
    print(planner.getPath(node1,node2))


if __name__ == '__main__':
    main()