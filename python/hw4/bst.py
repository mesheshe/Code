# Course: CS261 - Data Structures
# Student Name: Elias Meshesha
# Assignment:
# Description:


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

    def pop(self) -> object:
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self) -> object:
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

    def dequeue(self) -> object:
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
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value          # to store node's data
        self.left = None            # pointer to root of left subtree
        self.right = None           # pointer to root of right subtree

    def __str__(self):
        return str(self.value)

class BST:
    def __init__(self, start_tree=None) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using in-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "TREE pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # base case
        if not cur:
            return
        # store value of current node
        values.append(str(cur.value))
        # recursive case for left subtree
        self._str_helper(cur.left, values)
        # recursive case for right subtree
        self._str_helper(cur.right, values)

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        newNode = TreeNode(value)
        if self.root is None:
            self.root = newNode
        else:
            parentNode = None
            currNode = self.root
            while (currNode != None):
                parentNode = currNode
                if currNode.value <= value:
                    currNode = currNode.right
                else:
                    currNode = currNode.left
            if parentNode.value <= value:
                parentNode.right = newNode
            else:
                parentNode.left = newNode
            
    def findNode(self, node, value, parentNode = None):
        if node is None or node.value == value:
            return node, parentNode
        if value > node.value:
            return self.findNode(node.right, value, node)
        else:
            return self.findNode(node.left, value, node)

    def contains(self, value: object) -> bool:
        """
        TODO: Write this implementation
        """
        if self.root is None:
            return False
        node, parentNode = self.findNode(self.root, value)
        return node != None

    def get_first(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.root is None:
            return None
        return self.root.value
    
    def remove_first(self) -> bool:
        """
        TODO: Write this implementation 
        """
        if self.root is None:
            return False  
        elif self.root.right is None: # can also work for the check 
            self.root = self.root.left # self.root.right and self.root.left
        elif self.root.left is None:   # are none
            self.root = self.root.right
        else:
            parentSucc = None
            Succ = self.root.right
            while Succ.left is not None:
                parentSucc = Succ
                Succ = Succ.left
            if parentSucc is not None:  # only right subtree exists
                parentSucc.left = Succ.right
                Succ.right = self.root.right
            Succ.left = self.root.left
            self.root = Succ
        return True
    
    def replaceSuccessor(self, node, parentNode):
        parentSucc = None
        Succ = node.right
        while Succ.left is not None:
            parentSucc = Succ
            Succ = Succ.left
        if parentSucc is not None:
            parentSucc.left = Succ.right
        if node.right != Succ:
            Succ.right =  node.right
        if node.left != Succ:
            Succ.left = node.left
        if parentNode.value <= node.value:
            parentNode.right = Succ
        else:
            parentNode.left = Succ
        return True

    def remove(self, value) -> bool:
        """
        TODO: Write this implementation
        """
        node, parentNode = self.findNode(self.root, value)
        if node is None:
            return False
        if parentNode is None:
            return self.remove_first()
        elif node.right is None and node.left is None: # if it is a leaf
            if parentNode.value <= node.value:
                parentNode.right = None
            else:
                parentNode.left = None
        elif node.right is None and node.left is not None:
            if parentNode.value <= node.value:
                parentNode.right = node.left
            else:
                parentNode.left = node.left
        elif node.left is None and node.right is not None:
            if parentNode.value <= node.value:
                parentNode.right = node.right
            else:
                parentNode.left = node.right
        else:
            return self.replaceSuccessor(node, parentNode)
        return True
                
    def pre_order(self, q, currNode):
        if currNode is not None:
            q.enqueue(currNode.value)
            self.pre_order(q, currNode.left)
            self.pre_order(q, currNode.right)
        return q

    def pre_order_traversal(self) -> Queue:
        """
        TODO: Write this implementation
        """
        if self.root is None:
            return  Queue()
        return self.pre_order(Queue(), self.root)
    
    def in_order(self, q, currNode):
        if currNode is not None:
            self.in_order(q, currNode.left)
            q.enqueue(currNode.value)
            self.in_order(q, currNode.right)
        return q

    def in_order_traversal(self) -> Queue:
        """
        TODO: Write this implementation
        """
        if self.root is None:
            return Queue()
        return self.in_order(Queue(), self.root)

    def post_order(self, q, currNode):
        if currNode is not None:
            self.post_order(q, currNode.left)
            self.post_order(q, currNode.right)
            q.enqueue(currNode)
        return q

    def post_order_traversal(self) -> Queue:
        """
        TODO: Write this implementation
        """
        if self.root is None:
            return Queue()
        return self.post_order(Queue(), self.root)

    def by_level(self, q, q_throwaway = None):
        if q_throwaway is None:
            q_throwaway = Queue()
            q_throwaway.enqueue(self.root)
        if not q_throwaway.is_empty():
            currNode = q_throwaway.dequeue()
            q.enqueue(currNode.value)
            if currNode.left is not None:
                q_throwaway.enqueue(currNode.left)
            if currNode.right is not None:
                q_throwaway.enqueue(currNode.right)   
            self.by_level(q, q_throwaway)
        return q 

    def by_level_traversal(self) -> Queue:
        """
        TODO: Write this implementation
        """
        if self.root is None:
            return Queue()
        return self.by_level(Queue())

    def is_full_rec(self, node, que): 
        if node is not None:
            if (node.left is None and node.right is not None) or (node.left is not None and node.right is None):
                return False
            if node.left is not None:
                que.enqueue(node.left)
                que.enqueue(node.right)
        if que.is_empty():
            return True
        return self.is_full_rec(que.dequeue(), que)

    def is_full(self) -> bool:
        """
        TODO: Write this implementation
        """
        if self.root is None:
            return True 
        return self.is_full_rec(self.root, Queue())

    def is_complete_rec(self, node, height = 0, maxHeight = None, tof = True):
        # This stop condition makes sure that the leaves are all at the same level 
        # or only have a difference of 1
        if node is None: # ignore the additional 1 added due to none since it will cancel out 
            if maxHeight is None or height == maxHeight:
                return height, tof 
            elif tof and height == maxHeight - 1:
                tof = False
                return height, tof
            else:
                return -1, tof
        # This checks does the same thing as above except this is for self.root case since my stop condition above 
        # does not check for that since it only starts if node is None 
        if node is not None:
            if node.left is None and node.right is not None and not (node.right.left is None and node.right.right is None):
                maxHeight = -1 
            if node.right is None and node.left is not None and not (node.left.left is None and node.left.right is None):
                maxHeight = -1
        if node is not None and maxHeight != -1:
            maxHeight, tof = self.is_complete_rec(node.left,height + 1, maxHeight, tof)
            maxHeight, tof = self.is_complete_rec(node.right, height + 1, maxHeight, tof)
        return maxHeight, tof

    def is_complete(self) -> bool:
        """
        TODO: Write this implementation
        """
        if self.root is None:
            return True 
        maxHeight, tof = self.is_complete_rec(self.root)
        if maxHeight == -1:
            return False
        return True 

    def is_perfect(self) -> bool:
        """
        TODO: Write this implementation
        """
        if self.root is None:
            return True 
        height = self.height()
        size = self.size()
        return size == 2**(height + 1) - 1

    def s(self, node, q = None, q2 = None, count = 1):
        if q2 is None:
            q2 = Queue()
        if node is not None:
            if node.left is not None:
                q2.enqueue(node.left)
            if node.right is not None:
                q2.enqueue(node.right)
        if q2.is_empty():
            return count
        return self.s(q2.dequeue(), q, q2, count + 1)

    def size(self) -> int:
        """
        TODO: Write this implementation
        """
        if self.root is None:
            return 0
        return self.s(self.root)

    def h(self,node, height = 0, maxVal = 0):
        if node is None:
            height -= 1  # it counted the case where node is None, gotta uncount that
            if height > maxVal:
                return height 
            return maxVal
        if node is not None:
            maxVal = self.h(node.left, height + 1, maxVal)
            maxVal = self.h(node.right, height + 1, maxVal)
        return maxVal

    def height(self) -> int:
        """
        TODO: Write this implementation
        """
        if self.root is None:
            return -1
        return self.h(self.root)

    def leaves(self, node, counter = 0):
        if node is not None and node.left is None and node.right is None:
            return counter + 1
        if node is not None:
            counter = self.leaves(node.left, counter)
            counter = self.leaves(node.right, counter)
        return counter

    def count_leaves(self) -> int:
        """
        TODO: Write this implementation
        """
        if self.root is None:
            return 0
        return self.leaves(self.root)

    def unique(self, node, prev = None, curr = None, counter = 0):
        if prev is None:
            prev = Stack()
            curr = Stack()
            curr.push(None)
        if node is None:
            return counter
        if node is not None:
            counter = self.unique(node.left, prev, curr, counter)
            prev.push(curr.top())
            curr.push(node.value)
            if curr.top() != prev.top():
                counter+=1 
            counter = self.unique(node.right, prev, curr, counter)
        return counter

    def count_unique(self) -> int:
        """
        TODO: Write this implementation
        """
        if self.root is None:
            return 0
        return self.unique(self.root)

# BASIC TESTING - PDF EXAMPLES

if __name__ == '__main__':
    pass