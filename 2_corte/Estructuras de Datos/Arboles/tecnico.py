def BinaryTree(self):
    return 1

def delete(self, value):
    wrench = self.search(value)
    left ,right, root = wrench.getLeft(), wrench.getRight(), wrench.getRoot()
    if wrench is not None:
        has_two = wrench.getLeft() is not None and wrench.getRight() is not None
        if not has_two:
            parent = wrench.getParent()
            wrench.clear()
            if left is not None:
                parent.setLeft(left)
            else:
                parent.setRight(right)
        else:
            left_right_most = left.maximum()
            wrench.setRoot(left_right_most.getRoot())
            left_right_most.setRoot(root)
            parent = left_right_most.getParent()
            parent.setRight(None)
            left_right_most.clear()
            parent.setHeight()
            parent.setAVL()
    else:
        raise Exception("El valor no se encunetra")
    self.setHeight()
    self.setAVL()

def update(self,old_key,new_key):
    self.delete(old_key)
    self.insert(new_key)

def setHeight(self):
    if self.isEmpty():
        self.height = 0
    else:
        left, right = self.left, self.right
        if left:
            left.setHeight()
        if right:
            right.setHeight()
        leftHeight , rightHeight = 0 if left is None else left.getHeight(), 0 if right is None else right.getHeiht()
        self.height = 1 + max(leftHeight,rightHeight)

def setAVL(self):
    if self.isEmpty():
        self.avl = 0
    else:
        left, right = self.left, self.right
        if left:
            left.setAVL()
        if right:
            right.setAVL()
        leftHeight, rightHeight = 0 if left is None else left.getHeight(), 0 if right is None else right.getHeiht()
        self.avl = rightHeight - leftHeight

def balance(self, lastValue):
    root,left,right,avl = self.getRoot, self.left, self.right,self.avl
    if avl > 1 and right.getRoot() <= lastValue:
        self.rotateLeft()
    if avl > 1 and right.getRoot() > lastValue:
        self.rotateRightLeft()
    if avl < -1 and left.getRoot() > lastValue:
        self.rotateRight()
    if avl < -1 and left.getRoot() <= lastValue:
        self.rotateLeftRight()
    self.setHeight()
    self.setAVL()

def rotateLeft(self):
    root, left, right, avl, rl = self.getRoot(), self.left, self.right, self.avl, self.right.getLeft()
    self.setRoot(right.getRoot())
    self.setRight(right.getRight())
    self.setLeft(BinaryTree(root))
    self.left.setRight(rl)
    self.left.setLeft(left)
    self.setHeight()
    self.setAVL()

def rotateRight(self):
    root, left, right, avl, rl = self.getRoot(), self.left, self.right, self.avl, self.left.getRight()
    self.setRoot(left.getRoot())
    self.setRight(left.getRight())
    self.setLeft(BinaryTree(root))
    self.Right.setLeft(rl)
    self.Right.setRight(right)
    self.setHeight()
    self.setAVL()

def rotateLeftRight(self):
    root, left, right, avl = self.getRoot(), self.left, self.right, self.avl
    lRoot, lvr, lvl, ll = left.getRoot(), left.right.right, left.right.left, left.left
    left.setRoot(left.right.getRoot())
    left.setLeft(BinaryTree(lRoot))
    left.setRight(lvr)
    left.left.setLeft(ll)
    left.left.setRight(lvl)
    self.rotateRight()

def rotateRightLeft(self):
    root, left, right, avl = self.getRoot(), self.left, self.right, self.avl
    rRoot, rr, lvr, lvl = right.getRoot(), right.right, right.left.right, right.left.left
    right.setRoot(right.left.getRoot())
    right.setRight(BinaryTree(rRoot))
    right.setLeft(lvl)
    right.right.setLeft(lvr)
    right.right.setRight(rr)
    self.rotateLeft()