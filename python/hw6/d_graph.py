# Course: CS261 - Data Structures
# Author: Elias Meshesha 
# Assignment: 6
# Description: Builds a directed graph.

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
        Adds a new vertex to the graph. 
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
        Adds an edge to the graph.
        """
        if (src == dst) or (weight < 0) or (self.v_count <= src) or (self.v_count <= dst) or (src < 0) or (dst < 0):
            return
        # fix maybe right now we are not adding edges
        self.adj_matrix[src][dst] = weight

    def remove_edge(self, src: int, dst: int) -> None:
        """
        Remove edge from the graph
        """
        if (src == dst) or (self.v_count <= src) or (self.v_count <= dst) or (src < 0) or (dst < 0):
            return
        if self.adj_matrix[src][dst] != 0:
            self.adj_matrix[src][dst] = 0

    def get_vertices(self) -> []:
        """
        Return list of vertices in the graph 
        """
        arr = []
        for num in range(self.v_count):
            arr.append(num)
        return arr

    def get_edges(self) -> []:
        """
        Return list of edges in the graph 
        """
        arr = []
        for i in range(self.v_count):
            for j in range(self.v_count):
                if self.adj_matrix[i][j] != 0:
                    arr.append((i, j, self.adj_matrix[i][j]))
        return arr

    def is_valid_path(self, path: []) -> bool:
        """
        Return true if provided path is valid, False otherwise
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
        Return list of vertices visited during DFS search
        Vertices are picked in order
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
        Return list of vertices visited during BFS search
        Vertices are picked in order
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
        """
        Helper function that searches for cycle. Will return True if found otherwise 
        returns False.
        """
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
        Return True if graph contains a cycle, False otherwise
        """
        for i in range(self.v_count):
            if self.cycle_search(i, [i]):
                return True 
        return False

    def weight(self, k, l): 
        """
        Helper function that performs the Dijkstra's algo and returns the minimum
        distance between the given src and a given vertex.
        """
        m, q ={}, []
        m[k] = self.adj_matrix[k][k]
        heapq.heappush(q, m[k])

        while len(q) != 0:
            d_i = heapq.heappop(q)
            dupArr = []  # put all duplicates in here 
            for ele in m:
                if m[ele] == d_i:
                    dupArr.append(ele)
            for i in dupArr:
                for j in range(self.v_count):
                    d = self.adj_matrix[i][j]
                    if d != 0 and (j not in m or m[j] > d+d_i):
                        m[j] = d + d_i
                        heapq.heappush(q, m[j])
        return m[l]

    def dijkstra(self, src: int) -> []:
        """
        Returns an array that holds the minimum distance between src and a given
        vertex. inf if the path doesn't exist, 0 if src is the target, and finally 
        some distance for everything else.
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

if __name__ == '__main__':
    pass