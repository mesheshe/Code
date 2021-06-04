# Course: 
# Author: 
# Assignment: 
# Description:


class UndirectedGraph:
    """
    Class to implement undirected graph
    - duplicate edges not allowed
    - loops not allowed
    - no edge weights
    - vertex names are strings
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.adj_list = dict()

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            for u, v in start_edges:
                self.add_edge(u, v)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = [f'{v}: {self.adj_list[v]}' for v in self.adj_list]
        out = '\n  '.join(out)
        if len(out) < 70:
            out = out.replace('\n  ', ', ')
            return f'GRAPH: {{{out}}}'
        return f'GRAPH: {{\n  {out}}}'

    # ------------------------------------------------------------------ #

    def add_vertex(self, v: str) -> None:
        """
        Add new vertex to the graph
        """
        if v not in self.adj_list:
            self.adj_list[v] = []        

    def add_edge(self, u: str, v: str) -> None:
        """
        Add edge to the graph
        """
        if u == v:
            return 

        self.add_vertex(u)
        self.add_vertex(v)
        if u != v:
            if u not in self.adj_list[v]:
                self.adj_list[v].append(u)
                self.adj_list[v].sort(reverse=True)
            if v not in self.adj_list[u]:
                self.adj_list[u].append(v)
                self.adj_list[u].sort(reverse=True)

    def remove_edge(self, v: str, u: str) -> None:
        """
        Remove edge from the graph
        """
        if v in self.adj_list and u in self.adj_list:
            if u in self.adj_list[v]:
                self.adj_list[v].remove(u)
                self.adj_list[u].remove(v)

    def remove_vertex(self, v: str) -> None:
        """
        Remove vertex and all connected edges
        """
        if v in self.adj_list:
            for i in range(len(self.adj_list[v]) - 1, -1, -1):
                self.remove_edge(v, self.adj_list[v][i])
            self.adj_list.pop(v)

    def get_vertices(self) -> []:
        """
        Return list of vertices in the graph (any order)
        """
        ret = []
        for e in self.adj_list:
            ret.append(e)
        return ret

    def get_edges(self) -> []:
        """
        Return list of edges in the graph (any order)
        """
        ret =  []
        for v in self.adj_list:
            for u in self.adj_list[v]:
                if (u,v) not in ret and (v,u) not in ret:
                    ret.append((u,v))
        return ret     

    def is_valid_path(self, path: []) -> bool:
        """
        Return true if provided path is valid, False otherwise
        """

        if len(path) == 1:
            if path[0] not in self.adj_list:
                return False
        for num in range(0, len(path) - 1):        
            if path[num + 1] not in self.adj_list[path[num]]:
                return False
        return True 

    def dfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during DFS search
        Vertices are picked in alphabetical order
        """
        reachable, stack, x = [], [], True
        if v_start not in self.adj_list:
            return reachable
        stack.append(v_start)

        while len(stack) != 0 and x:
            v = stack.pop()
            if v not in reachable:
                reachable.append(v)
                if v != v_end:
                    for ele in self.adj_list[v]:
                        stack.append(ele)
                else:
                    x = False

        return reachable


    def bfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during BFS search
        Vertices are picked in alphabetical order
        """
        reachable, queue, x = [], [], True
        if v_start not in self.adj_list:
            return reachable
        queue.append(v_start)

        while len(queue) != 0 and x:
            v = queue.pop(0)
            if v not in reachable:
                reachable.append(v)
                if v != v_end:
                    for u in reversed(self.adj_list[v]):
                        queue.append(u)
                else:
                    x = False
        return reachable 

    def count_connected_components(self):
        """
        Return number of connected componets in the graph
        """
        ret, count, length = [], 0, self.adj_list.__len__()
        for v in self.adj_list:
            if v not in ret:
                count += 1
                ret += self.bfs(v)
        return count


    def cycle_search(self,v,L, path):
        if path.count(path[-1]) > 1:
            return True    
        boole = False
        for ele in L:
            if len(path) >= 2:
                if ele != path[-2]:
                    boole = self.cycle_search(ele, self.adj_list[ele], path + [ele])
            else:
                boole = self.cycle_search(ele, self.adj_list[ele], path + [ele])
            if boole:
                break
        return boole

    def has_cycle(self):
        """
        Return True if graph contains a cycle, False otherwise
        """
        for v in self.adj_list:
            if self.cycle_search(v, self.adj_list[v], [v]):
                return True
        return False
   


if __name__ == '__main__':

    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    """
    test_cases = (
    'add QH', 'remove FG', 'remove GQ', 'remove HQ',
    'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
    'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
    'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG',
    'add FG', 'remove GE')
    """
    test_cases = (
        'add QH','remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG' 
    )
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print('{:<10}'.format(case), g.has_cycle())
        if case == 'add EG':
            if g.is_valid_path(list('ACDQGEA')):
                print(True)
