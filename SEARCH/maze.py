import sys

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent  = parent
        self.action = action

class StackFrontier():
    def __init__(self):
        self.frontier = []  # represents a empty frontier

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)
    
    def empty(self): # check if the frontier is empty
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty():  
            raise Exception("empty frontier")
        else:
            node == self.frontier[-1]
            self.frontier = self.frontier[:-1]  # last-in first-out approach(DEEP-FIRST SEARCH)
            return node
        
class QueueFrontier(StackFrontier):

    def remove(self): 
        if self.empty():
            raise Exception('empty frontier')
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]  # first-in first-out approach(BREATH-FIRST SEARCH)
            return node
        
class Maze():

    def __init__(self, filename):

        # Read file and set height and width of the maze
        with open(filename) as f:
            contents = f.read()

        #validate start and goal
        if contents.count("A") != 1:
            raise Exception("Maze MUST have exactly one start point!")
        if contents.count("B") != 1:
            raise Exception("Maze MUST have exactly one goal!")
        
        #Determine height and width of maze
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        #keep track of walls
        self.walls = []
        for i in range(self.height):
