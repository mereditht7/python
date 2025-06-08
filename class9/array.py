class Array2D:
    def __init__(self, array):
        self.array = array
    
    def print_array(self):
        for x in self.array:
            for y in x:
                print(y)
    
my_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
twoDarray = Array2D(my_array)
print(twoDarray.print_array())

