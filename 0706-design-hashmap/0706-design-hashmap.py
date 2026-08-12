class MyHashMap(object):

    def __init__(self):
        self.l = [[] for _ in range(1000)]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        index = key % 1000

        for i in range(len(self.l[index])):
            if self.l[index][i][0] == key:
                self.l[index][i][1] = value
                return

        self.l[index].append([key, value])

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        index = key % 1000

        for pair in self.l[index]:
            if pair[0] == key:
                return pair[1]

        return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = key % 1000

        for i in range(len(self.l[index])):
            if self.l[index][i][0] == key:
                self.l[index].pop(i)
                return