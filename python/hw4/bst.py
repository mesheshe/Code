# Course: CS261 - Data Structures
# Student Name: Elias Meshesha
# Assignment: 4
# Description: The following code implements a binary search tree which has by creating
#              a bst class which has the following methods: add, contains, remove, get_first,
#              remove_first, pre-order-traversal, in-order-traversal, post-order-traversal, 
#              and etc.


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
        Adds the given value to the bst 
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
        """
        helper function that takes in a value and a node and traverse
        the tree starting from that node and if a node containing the value
        is found, the node as well as its parent is returned"""
        if node is None or node.value == value:
            return node, parentNode
        if value > node.value:
            return self.findNode(node.right, value, node)
        else:
            return self.findNode(node.left, value, node)

    def contains(self, value: object) -> bool:
        """
        returns true if a node containing the value passed in is found
        """
        if self.root is None:
            return False
        node, parentNode = self.findNode(self.root, value)
        return node != None

    def get_first(self) -> object:
        """
        gets the value of the root node if it exists otherwise returns None
        """
        if self.root is None:
            return None
        return self.root.value
    
    def remove_first(self) -> bool:
        """
        Removes the root node and returns True if done so otherwise returns False
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
        """
        helper function for the remove function, this helper function assumes 
        that we have gotten through all the preconditions and that we pass it in 
        the node we want to remove. This function will find the successor of this node
        and make that takes it place as well as give the right children of the successor
        to th successor's previous parent's left child Returns true once the replacement 
        is done 
        """
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
        Removes the first node found that contains the value given and returns True 
        after the operation has completed, otherwise returns False if not found. 
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
        """
        helper function that creates the queue by traversing the bst. Algo goes
        like this: if we see a node for the first time, we add it to the queue, then
        traverse left by recursively calling this function again and then we go right. 
        """
        if currNode is not None:
            q.enqueue(currNode.value)
            self.pre_order(q, currNode.left)
            self.pre_order(q, currNode.right)
        return q

    def pre_order_traversal(self) -> Queue:
        """
        Returns a queue that contains values gotten by traversing the bst in a
        pre-order-traversal manner. 
        """
        if self.root is None:
            return  Queue()
        return self.pre_order(Queue(), self.root)
    
    def in_order(self, q, currNode):
        """
        helper function that creates the queue by traversing the bst. Algo goes
        like this: We go all the way to the leftmost node, then we add the value
        to the queue, then we check if that value has a right node, if it does 
        it explores that path, otherwise it backs out a level to repeat the process 
        of writing down the value and then checking if a right node exists
        """
        if currNode is not None:
            self.in_order(q, currNode.left)
            q.enqueue(currNode.value)
            self.in_order(q, currNode.right)
        return q

    def in_order_traversal(self) -> Queue:
        """
        Returns a queue that contains values gotten by traversing the bst in a
        in-order-traversal manner. So Queue is sorted.
        """
        if self.root is None:
            return Queue()
        return self.in_order(Queue(), self.root)

    def post_order(self, q, currNode):
        """
        helper function that creates the queue by traversing the bst. Algo goes
        like this: Algo similar to in_order, except now we are also making sure that 
        when we write to queue, the value is for a node that has no right children
        """
        if currNode is not None:
            self.post_order(q, currNode.left)
            self.post_order(q, currNode.right)
            q.enqueue(currNode)
        return q

    def post_order_traversal(self) -> Queue:
        """
        Returns a queue that contains values gotten by traversing the bst in a
        post-order-traversal manner. 
        """
        if self.root is None:
            return Queue()
        return self.post_order(Queue(), self.root)

    def by_level(self, q, q_throwaway = None):
        """
        Helper function that returns a queue that is traversed by level
        Algo goes like this: It utilizes two queues. One throwawy, the other 
        a return queue. This function initializes the throwaway by enqueueing self.root.
        And while it is q_throwaway is not empty, it does the following:
        add the value of the node at the front of q_throwaway, to the return 
        queue. Then enqueue the left and right child of the dequeued node 
        respectively and if they exist. Then repeat. 
        """
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
        Returns a queue that traverses the tree by level
        """
        if self.root is None:
            return Queue()
        return self.by_level(Queue())

    def is_full_rec(self, node, que):
        """
        by level traversal. It first checks to make sure all internal nodes have
        two children, by checking if the current node only has one child, if that 
        passes, then the left child and the right child are added to the queue, after 
        making sure that the node is not a leaf node. The function is called recursively
        and for the node argument, we get it by dequeuing the queue. It returns true 
        if the queue is empty.  
        """ 
        if node is not None:
            if (node.left is None and node.right is not None) or (node.left is not None and node.right is None):
                return False
            if node.left is not None: # notice that we only need to check one, since node.right is also not none
                que.enqueue(node.left) # if this is true 
                que.enqueue(node.right)
        if que.is_empty():
            return True
        return self.is_full_rec(que.dequeue(), que)

    def is_full(self) -> bool:
        """
        Returns true if the bst is full otherwise returns false
        All internal nodes have two children
        """
        if self.root is None:
            return True 
        return self.is_full_rec(self.root, Queue())

    def is_complete_rec(self, node, height = 0, maxHeight = None, tof = True):
        """
        Helper function that determines whether a bst is complete, pre-order-traversal.
        Returns a tuple called a height which we care about and a bool which we don't 
        and is used internally. The height will return -1, if it is not complete, otherwise
        returns some number. This function, in a nutshell, looks at the height of the leaves,
        it makes sure that they are either all the same and if not, it makes sure that the 
        leaves going from left to right, only have a height change of 1 and that height 
        change only happens once, with the leftmost leaf's height > rightmost leaf's height.   
        """
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
        Returns true if the bst is complete otherwise returns false
        Except for the last level, every level before it is full, and the 
        for the last level, either it is full or if it is not, the node is
        added to the left child of the parent a level higher, before being
        added to the right.  
        """
        if self.root is None:
            return True 
        maxHeight, tof = self.is_complete_rec(self.root)
        return maxHeight != -1

    def is_perfect(self) -> bool:
        """
        Returns true if the bst is perfect otherwise returns false.
        The BST is full and all leaves have the same height 
        """
        if self.root is None:
            return True 
        height = self.height()
        size = self.size()
        return size == 2**(height + 1) - 1

    def s(self, node, q = None, q2 = None, count = 1):
        """
        Helper function that traverse the bst by level. It has a queue ADT which it 
        uses to store the left and rigt child of the current node (if they exist). 
        On each recurisve call, the queue is dqueued and the count is incremented by 1.
        When the queue is empty, it retuns the count.   
        """
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
        Returns the number of nodes in the binary search tree
        """
        if self.root is None:
            return 0
        return self.s(self.root)

    def h(self,node, height = 0, maxVal = 0):
        """
        Helper function that traverses the bst in a pre-order-traversal that
        checks first if the current node is a leaf and if so it increments
        counter and returns it. 
        """
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
        Returns the maximum depth of a binary tree, if it is empty it retuns
        -1 
        """
        if self.root is None:
            return -1
        return self.h(self.root)

    def leaves(self, node, counter = 0):
        """
        Helper function that traverses the bst in a pre-order-traversal that
        checks first if the current node is a leaf and if so it increments counter
        and returns it. 
        """
        if node is not None and node.left is None and node.right is None:
            return counter + 1     # + 1 because the current node needs to be added
        if node is not None:
            counter = self.leaves(node.left, counter)
            counter = self.leaves(node.right, counter)
        return counter

    def count_leaves(self) -> int:
        """
        Returns the count of leaves
        """
        if self.root is None:
            return 0
        return self.leaves(self.root)

    def unique(self, node, prev = None, curr = None, counter = 0):
        """
        Helper function that does an in-order-traversal, and utilizes 
        twp stacks, one named prev, and the other curr. prev gets curr.top()
        value pushed to it while curr gets the current node's value pushed to it.
        Then a comparison is done between these two stack's top(), and if they 
        are not the same, then the counter is incrememnted. Once this recursion 
        is done, it returns the counter.
        """
        if prev is None:
            prev = Stack()
            curr = Stack()
            curr.push(None)
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
        Counts the number of unique values in the binary search tree.
        """
        if self.root is None:
            return 0
        return self.unique(self.root)

# BASIC TESTING - PDF EXAMPLES

if __name__ == '__main__':
    pass