# Count set bits for 

#  (Binary 1100) 
# Iteration 1: n = 1100 & 1011 
#  n becomes 1000 (binary 8). count = 1.
# Iteration 2: n = 1000 & 0111 
#  n becomes 0000. count = 2

#input = 11 (1011)
#output = 3


def count_bits(n):
    count = 0
    while n:
        n = n & (n-1)
        count += 1
    return count
      
print(count_bits(11))  