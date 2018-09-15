def max_height(root):
    if root:
        return 1 + max(max_height(root.left), max_height(root.right))
    else:
        return -1
