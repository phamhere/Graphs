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
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

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

        def helper(node):
            if node not in visited:
                print(node)
                visited.add(node)

                for neighbor in self.vertices[node]:
                    helper(neighbor)

        helper(starting_vertex_id)
