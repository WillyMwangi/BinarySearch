def search(self, value):
    first = 0
    last = self.length - 1
    found = False
    count = 0
    in_list = False
    try:
        index = self.index(value)
        in_list = True
    except ValueError:
        index = -1
        in_list = False