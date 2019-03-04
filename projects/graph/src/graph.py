"""
Simple graph implementation
"""


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Graph:
    """Make a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist")

    def bft(self, starting_vertex_id):
        # create an empty queue
        q = Queue()
        # create an empty set of visited vertices
        visited = set()
        # put the starting vertex in our queue
        q.enqueue(starting_vertex_id)
        # while the queue is not empty
        while q.size() > 0:
            # dequeue the first node from the queue
            v = q.dequeue()
            # if that node has not been visited
            if v not in visited:
                # mark as visited
                print(v)
                visited.add(v)
                # then put all of it's children into the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex_id):
        # create an empty stack
        s = Stack()
        # create an empty set of visited vertices
        visited = set()
        # put the starting vertex in our stack
        s.push(starting_vertex_id)
        # while the stack is not empty
        while s.size() > 0:
            # pop the first node from the stack
            v = s.pop()
            # if that node has not been visited
            if v not in visited:
                # mark as visited
                print(v)
                visited.add(v)
                # then put all of it's children into the stack
                for neighbor in self.vertices[v]:
                    s.push(neighbor)

    def dft_recursion(self, starting_vertex_id):
        visited = set()
        # creating helper function since we need to store visited data

        def helper(node):
            if node not in visited:
                print(node)
                visited.add(node)

                for neighbor in self.vertices[node]:
                    # calling recursion function on neighbors
                    helper(neighbor)
        # initializing the recursive call on the first vertex
        helper(starting_vertex_id)

    def bfs(self, starting_vertex, target_vertex):
        # creating a queue starting with a tuple
        queue = [(starting_vertex, [starting_vertex])]
        paths = []
        while queue:
            # pops off the first element of the stack and tuple deconstructs it
            (vertex, path) = queue.pop(0)
            # loops through all neighbors of the vertex minus the path values
            for neighbor in self.vertices[vertex] - set(path):
                if neighbor == target_vertex:
                    paths.append(path + [neighbor])
                else:
                    queue.append((neighbor, path + [neighbor]))
        # sorting the paths based on length
        sorted(paths, key=len)
        # returning the shortest path or empty list if it wasn't found
        if len(paths) > 0:
            return paths[0]
        else:
            return paths

    def dfs(self, starting_vertex, target_vertex):
        # creating a stack starting with a tuple
        stack = [(starting_vertex, [starting_vertex])]
        paths = []
        while stack:
            # pops off the last element of the stack and tuple deconstructs it
            (vertex, path) = stack.pop()
            # loops through all neighbors of the vertex minus the path values
            for neighbor in self.vertices[vertex] - set(path):
                # if the neighbor is the target vertex, append to paths
                if neighbor == target_vertex:
                    paths.append(path + [neighbor])
                else:
                    stack.append((neighbor, path + [neighbor]))
        # sorting the paths based on length
        sorted(paths, key=len)
        # returning the shortest path or empty list if it wasn't found
        if len(paths) > 0:
            return paths[0]
        else:
            return paths
