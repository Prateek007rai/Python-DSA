#    for Size = 2
#    1       3
#      2   4
#        5
#        6
#        7

# Use maximum two loops

# Solution:
# 1 loop → for rows
# 1 loop → for spacing

def print_pattern(n):
    # Loop 1: top half — n rows, two numbers each
    for row in range(n):
        left_indent = " " * (row * 2)
        gap = " " * ((n - 1 - row) * 4 + 2)
        left_num = row + 1
        right_num = row + 1 + n
        print(left_indent + str(left_num) + gap + str(right_num))

    # Loop 2: bottom half — n+1 rows, one number each
    for row in range(n + 1):
        indent = " " * (n * 2)
        num = 2 * n + 1 + row
        print(indent + str(num))

print_pattern(3)