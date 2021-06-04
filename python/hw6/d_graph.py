# Course: CS261 - Data Structures
# Author:
# Assignment:
# Description:

import heapq 

class DirectedGraph:
    """
    Class to implement directed weighted graph
    - duplicate edges not allowed
    - loops not allowed
    - only positive edge weights
    - vertex names are integers
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency matrix
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.v_count = 0
        self.adj_matrix = []

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if self.v_count == 0:
            return 'EMPTY GRAPH\n'
        out = '   |'
        out += ' '.join(['{:2}'.format(i) for i in range(self.v_count)]) + '\n'
        out += '-' * (self.v_count * 3 + 3) + '\n'
        for i in range(self.v_count):
            row = self.adj_matrix[i]
            out += '{:2} |'.format(i)
            out += ' '.join(['{:2}'.format(w) for w in row]) + '\n'
        out = f"GRAPH ({self.v_count} vertices):\n{out}"
        return out

    # ------------------------------------------------------------------ #

    def add_vertex(self) -> int:
        """
        TODO: Write this implementation
        """
        self.v_count += 1

        if self.adj_matrix == []:
            self.adj_matrix.append([0])
            return self.v_count

        arr = [0]
        for i in range(self.v_count - 1):
            self.adj_matrix[i].append(0)
            arr.append(0)

        self.adj_matrix.append(arr)
        
        return self.v_count

    def add_edge(self, src: int, dst: int, weight=1) -> None:
        """
        TODO: Write this implementation
        """
        if (src == dst) or (weight < 0) or (self.v_count <= src) or (self.v_count <= dst) or (src < 0) or (dst < 0):
            return
        # fix maybe right now we are not adding edges
        self.adj_matrix[src][dst] = weight

    def remove_edge(self, src: int, dst: int) -> None:
        """
        TODO: Write this implementation
        """
        if (src == dst) or (self.v_count <= src) or (self.v_count <= dst) or (src < 0) or (dst < 0):
            return
        if self.adj_matrix[src][dst] != 0:
            self.adj_matrix[src][dst] = 0

    def get_vertices(self) -> []:
        """
        TODO: Write this implementation
        """
        arr = []
        for num in range(self.v_count):
            arr.append(num)
        return arr

    def get_edges(self) -> []:
        """
        TODO: Write this implementation
        """
        arr = []
        for i in range(self.v_count):
            for j in range(self.v_count):
                if self.adj_matrix[i][j] != 0:
                    arr.append((i, j, self.adj_matrix[i][j]))
        return arr

    def is_valid_path(self, path: []) -> bool:
        """
        TODO: Write this implementation
        """
        if len(path) == 0 or len(path) == 1:
            if len(path) == 1:
                if path[0] > self.v_count:
                    return False
            return True
        for i in range(1, len(path)):
            prev = path[i - 1]
            curr = path[i]
            if self.adj_matrix[prev][curr] == 0:
                return False
        return True 

    def dfs(self, v_start, v_end=None) -> []:
        """
        TODO: Write this implementation
        """
        reachable, stack, x = [], [], True
        if v_start < 0 or v_start >= self.v_count:
            return []
        stack.append(v_start)

        while len(stack) != 0 and x:
            i = stack.pop()
            if i not in reachable:
                reachable.append(i)
                if i != v_end:
                    for j in range(self.v_count - 1, -1, -1):
                        if self.adj_matrix[i][j] != 0:
                            stack.append(j)
                else:
                    x = False
        return reachable


    def bfs(self, v_start, v_end=None) -> []:
        """
        TODO: Write this implementation
        """
        reachable, queue, x = [], [], True
        if v_start < 0 or v_start >= self.v_count:
            return reachable
        queue.append(v_start)

        while len(queue) != 0 and x:
            i = queue.pop(0)
            if i not in reachable:
                reachable.append(i)
                if i != v_end:
                    for j in range(self.v_count):
                        if self.adj_matrix[i][j] != 0:
                            queue.append(j)
                else:
                    x = False
        return reachable

    def cycle_search(self, i, path):
        if path.count(path[-1]) > 1:
            return True
        bool = False
        for j in range(self.v_count):
            if self.adj_matrix[i][j] != 0:
                bool = self.cycle_search(j, path + [j])
            if bool:
                break    
        return bool

    def has_cycle(self):
        """
        TODO: Write this implementation
        """
        for i in range(self.v_count):
            if self.cycle_search(i, [i]):
                return True 
        return False

    def weight(self, k, l): 
        m, reachable, q ={}, []
        m[k] = self.adj_matrix[k][k]
        heapq.heappush(q, m[k])

        while len(q) != 0:
            d_i = heapq.heappop(q)
            dupArr = []  # put all duplicates in here 
            for ele in m:
                if m[ele] == d_i:
                    dupArr.append(ele)
            for i in dupArr:
                if i not in reachable: # I feel like I don't need
                    reachable.append(i) # these two lines 
                    for j in range(self.v_count):
                        d = self.adj_matrix[i][j]
                        if d != 0 and (j not in m or m[j] > d+d_i):
                            m[j] = d + d_i
                            heapq.heappush(q, m[j])
        return m[l]

    def dijkstra(self, src: int) -> []:
        """
        TODO: Write this implementation
        """
        arr = []
        for j in range(self.v_count):
            temp = self.bfs(src, j)
            if j not in temp:
                arr.append(float('inf'))
            elif len(temp) == 1:
                arr.append(0)
            else:
                arr.append(self.weight(src, j))
        return arr

import math  # For testing purposes only 
if __name__ == '__main__':
    a = [ 0,  0,  0,  7,  0,  0,  0,  0,  0,  0,  0,  0,
        13,  0,  0,  0,  0,  0,  0,  3,  0,  0,  0,  0,
         0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
         0,  0,  0,  0,  0,  0,  0,  0,  9,  0,  0,  0,
         0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        18,  0,  0,  0,  0,  0,  0,  0,  0, 18,  0,  0,
         0,  0,  0,  0,  0,  0,  0,  0,  0, 17,  0,  0,
         0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
         0,  0,  0,  0,  5,  0,  1,  0,  0,  0,  0,  0,
         0,  0,  0,  0,  0,  0, 11,  0,  0,  0,  0,  0,
         0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
         0,  0,  0,  0,  0,  0,  0,  7,  0,  7,  0,  0
    ]

    side =  int(math.sqrt(len(a)))
    edges = []
    for i in range(side):
        for j in range(side):
            if a[i*side + j] != 0:
                edges.append((i,j, a[i*side + j]))

    print("\nPDF - dijkstra() example 1")
    print("--------------------------")
    g = DirectedGraph(edges)
    print(g)
    print(f'DIJKSTRA {5} {g.dijkstra(5)}')
    #28 needs to be 11

