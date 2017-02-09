class BinarySearch(list):
    def __init__(self, a, b):  # list of length a and intervals b between the elements
        self.a = a
        self.b = b

        for i in range(self.a):
            list.append(self, self.b)
            self.b += b
            i += 1