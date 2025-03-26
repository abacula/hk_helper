class GetConnections:
    def __init__(self,filename):
        self.f = open(filename, "r")
        
    def getConnections(self):
        line = self.f.readline()
        while self.f.readable() and "CHECKED TRANSITIONS" not in line:
            line = self.f.readline()[:-1]
            # print(line)
        
        # now at transitions
        nodes = []
        nodeLoc = []
        while line:
            line = self.f.readline().strip()
            words = line.split("-->")
            if len(words) < 2:
                break

            node1 = words[0].split("[")
            node2 = words[1].split("[")

            if node1[0][0] == "*":
                node1[0] = node1[0][1:]

            node1[1] = node1[1].strip()[:-1]
            
            node2[0] = node2[0].strip()
            node2[1] = node2[1].strip()[:-1]

            nodes.append([node1[0], node1[1],node2[0],node2[1]])
            nodeLoc.append((node1[0],node2[0]))
        return nodes,nodeLoc
          

def main(args=None):
    c = GetConnections("HelperLog.txt")
    nodes,nodeLoc = c.getConnections()
    print(nodeLoc)

if __name__ == '__main__':
    main()

