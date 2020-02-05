import operator 
from functools import reduce

def combine(my_list, your_list): 
    return reduce(operator.add, zip(my_list, your_list)) 
      
my_list = [11, 22, 33] 
your_list = [1, 2, 3] 
print(combine(my_list, your_list))