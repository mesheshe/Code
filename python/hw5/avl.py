# Course: CS261 - Data Structures
# Student Name: Elias Meshesha 
# Assignment: 5
# Description: Builds an AVL tree.


import random


class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self):
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self):
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self):
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    AVL Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Initialize a new AVL node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0

    def __str__(self):
        return 'AVL Node: {}'.format(self.value)


class AVL:
    def __init__(self, start_tree=None) -> None:
        """
        Initialize a new AVL tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate AVL with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of AVL in human-readable form using pre-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "AVL pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if cur:
            values.append(str(cur.value))
            self._str_helper(cur.left, values)
            self._str_helper(cur.right, values)

    def is_valid_avl(self) -> bool:
        """
        Perform pre-order traversal of the tree. Return False if there
        are any problems with attributes of any of the nodes in the tree.

        This is intended to be a troubleshooting 'helper' method to help
        find any inconsistencies in the tree after the add() or remove()
        operations. Review the code to understand what this method is
        checking and how it determines whether the AVL tree is correct.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        s = Stack()
        s.push(self.root)
        while not s.is_empty():
            node = s.pop()
            if node:
                # check for correct height (relative to children)
                l = node.left.height if node.left else -1
                r = node.right.height if node.right else -1
                if node.height != 1 + max(l, r):
                    return False

                if node.parent:
                    # parent and child pointers are in sync
                    if node.value < node.parent.value:
                        check_node = node.parent.left
                    else:
                        check_node = node.parent.right
                    if check_node != node:
                        return False
                else:
                    # NULL parent is only allowed on the root of the tree
                    if node != self.root:
                        return False
                s.push(node.right)
                s.push(node.left)
        return True

    # -----------------------------------------------------------------------
    
    def find(self, node, value, tof = True):
        """
        Takes in a value and returns the node which match the value. If false it will 
        return the parent node or the node if already exists.
        """
        if node is not None:
            if node.value > value:
                if node.left is not None:
                    return self.find(node.left, value, tof)
                else:
                    return node
            else:
                if not tof and node.value == value:
                    return node
                elif node.right is not None:
                    return self.find(node.right, value, tof)
                else:
                    return node 
                    
    def updateHeight(self, node):
        """
        Takes in a node and updates the height of the node and all 
        ancestors before it. How a height is calculated is by using
        max(node.left.height + node.right.height) + 1, for non-leaf.
        For leaves height = 0
        """
        #node is being updated 
        if node.left is not None and node.right is not None:
            if node.left.height > node.right.height:
                node.height = node.left.height + 1
            else:
                node.height = node.right.height + 1
        elif node.left is None and node.right is None:
            node.height = 0
        elif node.left is None:  
            node.height = node.right.height + 1
        elif node.right is None:
            node.height = node.left.height + 1
        
        while node.parent is not None:
            # parents are at least of height one
            parent = node.parent
            left, right = parent.left, parent.right
            if left is not None and right is not None:
                if left.height > right.height:
                    parent.height = left.height + 1
                else:
                    parent.height = right.height + 1
            elif right is None:
                parent.height = left.height + 1
            else:
                parent.height = right.height + 1
            node = node.parent

    def rotateRight(self, node):
        """
        Takes in a node and performs a right rotation assuming that all pre-conditions 
        are met. Updates the parent for all nodes involved. 
        """
        # point the parents to it 
        parent = None
        if node.parent is not None:
            parent = node.parent
        leftNode = node.left
        node.left = leftNode.right
        if node.left is not None:
            node.left.parent = node
        leftNode.right = node
        if parent is None:
            self.root = leftNode
            self.root.parent = None
        else:
            leftNode.parent = parent
            if parent.right == node:
                parent.right = leftNode
            else:
                parent.left = leftNode
        node.parent = leftNode
        self.updateHeight(node)

    def rotateLeft(self,node):
        """
        Takes in a node and performs a left rotation assuming that all pre-conditions 
        are met. Updates the parent for all nodes involved. 
        """
        # you got to think of this like a linked list 
        parent = None
        if node.parent is not None:
            parent = node.parent 
        rightNode = node.right
        node.right = rightNode.left
        if node.right is not None:
            node.right.parent = node
        rightNode.left = node
        if parent is None:
            self.root = rightNode
            self.root.parent = None
        else:
            rightNode.parent = parent
            if parent.right == node:
                parent.right = rightNode
            else:
                parent.left = rightNode 
        node.parent = rightNode
        self.updateHeight(node)

    def rebalance(self, node):
        """
        Takes in a node and rebalances the node starting from that node and all parents involved
        Everything below that node is assumed to already be balanced.
        """
        # we are starting from the node we just added in, so everything below 
        # that is already balanced, so we don't need to worry, so we really 
        # should care about the case where node.left and node.right are both not
        # None
        if node is not None:
            if node.left is not None and node.right is not None:
                height = node.right.height - node.left.height
                if height == 2: # right heavy, now need to check if it is right right or right left
                    if node.right.left is None or (node.right.right is not None and node.right.left.height <= node.right.right.height):
                        self.rotateLeft(node) 
                    else: # right left 
                        self.rotateRight(node.right)  # this extra step is required to make it right right heavy
                        self.rotateLeft(node) 
                elif height == -2: #left heavy, now need to check if it is left left or left right
                    if node.left.right is None or (node.left.left is not None or node.left.left.height >= node.left.right.height):
                        self.rotateRight(node)
                    else: # left right, rotate left first then right 
                        self.rotateLeft(node.left)  # this extra step is required to make it left left heavy
                        self.rotateRight(node)
            elif node.right is None and node.height == 2:
                # we need to make sure that it is left left 
                if node.left.right is None or (node.left.left is not None and node.left.left.height >= node.left.right.height):
                    self.rotateRight(node)
                else:
                    self.rotateLeft(node.left)  # this extra step is required to make it left left heavy
                    self.rotateRight(node)
            elif node.left is None and node.height == 2:
                # we need to make sure that it is right right 
                if node.right.left is None or (node.right.right is not None and node.right.right.height >= node.right.left.height): 
                    self.rotateLeft(node)
                else:
                    self.rotateRight(node.right)  # this extra step is required to make it right right heavy
                    self.rotateLeft(node)
            self.rebalance(node.parent)     
            
    def add(self, value: object) -> None:
        """
        Adds a node containing value to the AVL tree, if it doesn't already exist
        """
        node = TreeNode(value)
        if self.root is None:
            self.root = node
            return
        # from this point on we are dealing with thing with parents
        parentNode = self.find(self.root, value, False)
        if parentNode.value == value: # duplicates begone
            return
        if parentNode.value > value:
            parentNode.left = node
        else:
            parentNode.right = node
        node.parent = parentNode
        self.updateHeight(node)
        self.rebalance(node)

    def removeRoot(self):
        """
        This function is called to remove a node that is a root.
        """
        if self.root.left is None and self.root.right is None:
            self.root = None 
            return
        elif self.root.left is None:
            self.root = self.root.right
        elif self.root.right is None:
            self.root = self.root.left
        else: # self.root has both left and right
            succ = self.root.right
            while succ.left is not None:
                succ = succ.left
            succ.left = self.root.left
            succ.left.parent = succ
            parent = None
            if succ.parent is not self.root:
                parent = succ.parent
                parent.left = succ.right
                if parent.left is not None:
                    parent.left.parent = parent
                succ.right = self.root.right
                succ.right.parent = succ
            else:
                succ.right = self.root.right.right
                if succ.right is not None:
                    succ.right.parent = succ
            self.root = succ
            self.root.parent = None 
            if parent is not None:
                self.updateHeight(parent)
                self.rebalance(parent)
                return
        self.root.parent = None
        self.updateHeight(self.root)
        self.rebalance(self.root)
        
    def removeNonRoot(self, node):
        """
        This function is called to removes a node if it is non-root.
        """
        parent = node.parent
        if node.left is None and node.right is None:
            if node == parent.left:
                parent.left = None 
            else:
                parent.right = None
            self.updateHeight(parent) #updating and rebalancing the parent 
            self.rebalance(parent)    #cause everything below it is already balanced
        elif node.left is None:
            if node == parent.left:
                parent.left = node.right
            else:
                parent.right = node.right
            node.right.parent = parent
            self.updateHeight(parent)
            self.rebalance(parent)
        elif node.right is None:
            if node == parent.left:
                parent.left = node.left
            else:
                parent.right = node.left
            node.left.parent = parent
            self.updateHeight(parent)
            self.rebalance(parent)
        else: # node has both left and right 
            succ = node.right
            while succ.left is not None:
                succ = succ.left
            succ.left = node.left
            succ.left.parent = succ
            succParent = None
            if succ.parent is not node:
                succParent = succ.parent
                succ.parent.left = succ.right
                if succParent.left is not None:
                    succParent.left.parent = succParent
            if node.right != succ:
                succ.right = node.right
            else:
                succ.right = node.right.right
            if succ.right is not None:
                succ.right.parent = succ
            if parent.left == node:
                parent.left = succ
            else:
                parent.right = succ
            succ.parent = parent 
            if succParent is not None:
                self.updateHeight(succParent)
                self.rebalance(succParent)
            else:
                self.updateHeight(succ)
                self.rebalance(succ)
        return

    def remove(self, value: object) -> bool:
        """
        Removes a node containing value from the tree and returns True if it does so
        """
        if self.root is None:
            return False 
        node = self.find(self.root, value, False)
        if node.value != value:
            return False
        if node == self.root:
            self.removeRoot()
        else:
            self.removeNonRoot(node)
        return True 
        

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':
    test_cases = (
        (1, 2, 3), #RR
        (3, 2, 1), #LL
        (1, 3, 2), #RL
        (3, 1, 2), #LR
    )
