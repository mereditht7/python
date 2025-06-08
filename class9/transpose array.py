class Array2D:
    def __init__(self, array):
        self.array = array
    
    def get_transpose(self):
        transposed = []
        for x in range(len(self.array)):
            new_row = []
            for y in range (len(self.array[0])):
                new_row.append(self.array[y][x])
            transposed.append (new_row)
        print(transposed)
        self.array=transposed
    
    def get_allign(self):
        for x in self.array:
            print(x)
        print()

    def get_reverse(self):
        reverse = []
        for x in range(len(self.array) -1, -1, -1):
            new_row = []
            for y in range (len(self.array) -1, -1, -1):
                new_row.append(self.array[x][y])
            reverse.append (new_row)
        print(reverse)
        self.array = reverse

    def get_reverse2(self):
        list = self.array
    

my_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
twoDarray = Array2D(my_array)
"""
print(twoDarray.get_allign())
print(twoDarray.get_transpose())
print(twoDarray.get_allign())
"""
print(twoDarray.get_reverse())
print(twoDarray.get_allign())