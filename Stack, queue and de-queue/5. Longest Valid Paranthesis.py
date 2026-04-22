# Time: O(n),Space: O(n)

# i/p: ")()())"
# o/p: 4

def long_paranthesis(s):
    stack = [-1]
    res = 0

    for i in range(len(s)):
        print(i,"for", stack)
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                res = max(res, i - stack[-1])
    return res

print(long_paranthesis(")()())"))
