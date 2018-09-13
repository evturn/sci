def ancestors(root, val):
    if root == None:
        return None
    if root.data == val:
        return [val]

    leftVals = ancestors(root.left, val)
    if leftVals != None:
        return [root.data] + leftVals

    rightVals = ancestors(root.right, val)
    if rightVals != None:
        return [root.data] + rightVals

    return None

def lowest_common_ancestor(root, x, y):
    l = ancestors(root, x)
    r = ancestors(root, y)
    lca = None

    for i in range(min(len(l), len(r))):
        if r[i] == l[i]:
            lca = l[i]
        else:
            break

    return lca
