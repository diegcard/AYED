def checkState(self):
    self.setHeight()
    self.setAVL()
    if abs(self.avl) > 1:
        self.balanceTree()
    return self


def balanceTree(self):
    if self.avl < -1 and self.getAVLFactorT(self.left) <= 0:
        self.rotateRight()
    if self.avl > 1 and self.getAVLFactorT(self.right) >= 0:
        self.rotateLeft()
    if self.avl < -1 and self.getAVLFactorT(self.left) > 0:
        self.rotateRightLeft()
    if self.avl > 1 and self.getAVLFactorT(self.right) < 0:
        self.rotateLeftRight()
    self.setHeight()
    self.setAVL()


def getAVLFactorT(self, tr):
    if tr and isinstance(tr, BinaryTree):
        return tr.avl
    return 0