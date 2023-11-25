# class TreeNode:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# def tree_minimum(root):
#     if root is None:
#         return None
#     if root.left is None:
#         return root.val
#     return tree_minimum(root.left)
#
#
# def tree_maximum(root):
#     if root is None:
#         return None
#     if root.right is None:
#         return root.val
#     return tree_maximum(root.right)


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.parent = None
        self.left = left
        self.right = right
        if left is not None:
            left.parent = self
        if right is not None:
            right.parent = self


def tree_maximum(root):
    if root is None:
        return None
    if root.right is None:
        return root
    return tree_maximum(root.right)


def tree_predecessor(root):
    if root is None:
        return None
    if root.left is not None:
        return tree_maximum(root.left)
    p = root.parent
    while p is not None and root == p.left:
        root = p
        p = p.parent
    return p