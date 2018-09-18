def is_balanced(s):
    opening = ['(', '{', '[']
    closing = [')', '}', ']']
    stack = []

    for c in s:
        if c in opening:
            stack.append(c)
        elif c in closing:
            open = stack.pop()

            if opening.index(open) != closing.index(c):
                return False
    
    return not len(stack)
