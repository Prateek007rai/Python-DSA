# Practice
# 2nd highest number in array 

def find_num(arr):
    first = second = float('-inf')

    for num in arr:
        if num > first: 
            second = first
            first = num
        elif first > num > second:
            second = num
    return second
print(find_num([34,45,53,21,24,64,54]))


# String compression

def compress(str1):
    res = ''
    count = 1

    for i in range(1, len(str1)):
        if str1[i] == str1[i-1]:
            count += 1
        else:
            res = res + str1[i-1] + str(count)
            count = 1
    
    res = res + str1[-1] + str(count) 
    return res

print(compress("aaaaaa"))
