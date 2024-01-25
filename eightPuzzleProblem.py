import heapq
import copy

class priority_queue:
    def __init__(self):
        self.heap = []

    def push(self, x):
        heapq.heappush(self.heap, x)
    
    def pop(self):
        return heapq.heappop(self.heap)
    
    def empty(self):
        #Determines if heap is empty
        if not self.heap:
            return True
        else:
            return False

class node:
    def __init__(self, parent_node, puzzle: list, empty_tile_position: int, num_misplaced_tiles: int, num_moves: int):
        self.parent_node = parent_node
        self.puzzle: list = puzzle
        self.empty_tile_position: int = empty_tile_position
        self.num_misplaced_tiles: int = num_misplaced_tiles
        self.num_moves: int = num_moves

    #Used for priority queue to compare nodes
    def __lt__(self, next):
        return self.num_misplaced_tiles < next.num_misplaced_tiles

#Creates child node with input of puzzle after empty space has been moved
def createNode(puzzle: list, parent_node: node, num_moves: int, goal_state: list):
     num_misplaced_tiles = calculateMisplacedTiles(puzzle, goal_state)
     return node(parent_node, puzzle, puzzle.index(0), num_misplaced_tiles, num_moves)

#Calculates number of misplaced tiles in a node
def calculateMisplacedTiles(puzzle: list, goal_state: list):
    count_misplaced = 0
    for i in range(len(puzzle)):
        if(puzzle[i] != goal_state[i]):
            count_misplaced += 1
    return count_misplaced

#Prints path from root to solution
def printPath(root: node):
    if root == None:
        print("START OF PUZZLE")
        return
    printPath(root.parent_node)
    print(root.puzzle) 


def solve(initial_puzzle: list, goal_state: list):
     queue = priority_queue()
     num_misplaced_tiles = calculateMisplacedTiles(initial_puzzle, goal_state)
     root = node(None, initial_puzzle, initial_puzzle.index(0), num_misplaced_tiles, 0 )

     queue.push(root)

     while not queue.empty():
         least_cost_unexpanded_node: node = queue.pop()

         if least_cost_unexpanded_node.num_misplaced_tiles == 0:
             printPath(least_cost_unexpanded_node)
             print("SOLUTION WITH {} MOVES".format(least_cost_unexpanded_node.num_moves))
             return
         
         
         empty_tile = least_cost_unexpanded_node.puzzle.index(0)
         #Generates children nodes
         for possible_move in possible_moves[empty_tile]:
             new_puzzle = copy.deepcopy(least_cost_unexpanded_node.puzzle)
             new_puzzle[empty_tile] = least_cost_unexpanded_node.puzzle[possible_move]
             new_puzzle[possible_move] = 0
             child = createNode(new_puzzle, least_cost_unexpanded_node, least_cost_unexpanded_node.num_moves + 1, goal_state)

             queue.push(child)




goal_state = [1,2,3,4,5,6,7,8,0]
possible_moves = [[1,3],[0,2,4],[1,5],[0,4,6],[1,3,5,7],[2,4,8],[3,7],[4,6,8],[7,5]]
start_puzzle = [1,2,3,4,0,8,7,6,5]

solve(start_puzzle, goal_state)