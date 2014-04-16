__author__ = 'danbox'


class UF:

    def __init__(self, n):
        self._n = n
        self._id = []
        for i in range(n):
            self._c = self._id.append(i)
        self._l = []
        for i in range(n):
            temp = [i]
            self._l.append(temp)

    def getid(self):
        return self._id

    def getl(self):
        return self._l

    def __str__(self):
        return "id: " + str(self._id) + '\n' + "l: " + str(self.getl())

    def getn(self):
        return self._n

    def find(self, elem):
        for i, u in enumerate(self._l):
            if u is not None:
                if elem in u:
                    return i

    def union(self, dest, src):
        dest_id = self.find(dest)
        src_id = self.find(src)
        if dest_id == src_id:
            return False
        else:
            self._id[src_id] = dest_id
            self._l[dest_id].extend(self._l[src_id])
            self._l[src_id] = None
            return True