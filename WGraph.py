__author__ = 'danbox'

import UF
import copy

class WGraph:

    def __init__(self, num_verts, edge_list):
        self._m = len(edge_list)
        self._verts = [[] for i in range(num_verts)]
        self._weights = [[] for i in range(num_verts)]
        for u, v, w in edge_list:
            self._verts[u].append(v)
            self._weights[u].append(w)

    def getn(self):
        return len(self._verts)

    def getm(self):
        return self._m

    def getEdges(self):
        edge_list = []
        for i in range(self.getn()):
            for k, j in enumerate(self._verts[i]):
                edge_list.append((i, j, self._weights[i][k]))
        return edge_list

    def MST(self):
        uf = UF.UF(self._verts)
        sortedWeights = copy.deepcopy(self._weights)
        sortedWeights.sort(key=lambda x: x[1])



    def __str__(self):
        temp = ""
        for i in range(self.getn()):
            zipped = zip(self._verts[i], self._weights[i])
            temp += str(i).rjust(3) + ": " + str(list(zipped)) + '\n'

        return "n = " + str(self.getn()) + " m = " + str(self.getm()) + '\n' + temp


def readGraph(filename):
    edge_list = []
    fp = open(filename, 'r')
    n = int(fp.readline())
    for line in fp:
        u, v, w = [int(x) for x in line.split(',')]
        edge_list.append((u, v, w))
    return WGraph(n, edge_list)

if __name__ == '__main__':
    g = readGraph('winput.txt')
    print(g)