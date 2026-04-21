# Time: O(n), Space: O(n)

# i/p: (A+B)*C
# o/p: AB+C*

def infix_to_postfix(s):
    res = ''
    stack = []
    prec = {'(': 0,'+': 1, '-': 1, '/': 2, '*': 2, '^': 3}

    for ch in s:
        if ch.isalnum():
            res = res + ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            # pop until meet '('
            while stack and stack[-1] != '(':
                res = res + stack.pop()
            stack.pop() 
        else:
            # insert operators, check if in stack there is high prec operator present or not
            while stack and stack != '(' and prec[ch] <= prec[stack[-1]]:
                res = res + stack.pop()
            stack.append(ch)

    # now pop stack until it is empty
    while stack:
        res = res + stack.pop()
    return res

print(infix_to_postfix("(A+B)*C"))

