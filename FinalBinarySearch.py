"""
BINARY SEARCH
   Create a Class called BinarySearch that inherits from the list class
   -->the __init__() takes two integers as parameters, a and b.
   -->a is the length of the list to be created.
   -->b is the step or difference between consecutive values.
   -->It should also initialize an instance variablelength`, that returns the number of elements in the array

     SEARCH METHOD
     create another method called search,
     -->it will take just one argument which is the value you are to find.
     -->The search function should return a dictionary object, which contains

    IMPLEMENTATION OF SEARCH
    The search method should implement the binary search algorithm, each time you iterate, you should increase the count, to test how efficient your implementation is.
"""


class BinarySearch(list):
    def __init__(self, a, b):  # the __init__() takes two integers as parameters, a and b.
        self.a = a
        self.b = b

        for i in range(self.a):
            list.append(self, self.b)
            self.b += b  # b is the interval between consecutive values.
            i += 1

        self.length = i

    def search(self, value):  # create another method called search which takes one argument
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

        while first <= last and not found and in_list and value != self[last]:
            midpoint = (first + last) // 2
            mid_value = self[midpoint]

            if mid_value == value:
                found = True
                count += 1
                index = midpoint
            else:
                if value < mid_value:
                    last = midpoint - 1
                    count += 1
                else:
                    first = midpoint + 1
                    count += 1

        return {"count": count, "index": index}