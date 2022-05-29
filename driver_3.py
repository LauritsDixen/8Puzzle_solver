import time

class Board(object):
    # Board class
    
    def __init__(self,board):
        # Initiates a Board
        self.board = board
       
    def getBoard(self):
        # Returns copy of board(list) - not for changing the board
        return self.board[:]
    
    def __str__(self):
        # Prints the boardstate in a fancy way, for debugging
        board = self.getBoard()
        return str(board[0:3]) + '\n' + str(board[3:6]) + '\n' + str(board[6:9])
       
    def getFreePosisition(self):
        # Returns integer that is the free place at the board
        return self.getBoard().index(0)
    
    def getAvailMoves(self):
        # Return a list of strings with available moves
        moves = []
        fP = self.getFreePosisition()
        
        if fP > 2:
            moves.append('Up')
        if fP < 6:
            moves.append('Down')
        if not fP % 3 == 0:
            moves.append('Left')
        if not fP % 3 == 2:
            moves.append('Right')
        return moves
    
    def move(self,move):
        # Makes a move, take a move(string) and outputs a list with the new boardstate
        
        board = self.getBoard()

        if move == 'Up':
            a, b = board.index(0), board.index(0) - 3
            board[b], board[a] = board[a], board[b]
            return board
        
        if move == 'Down':
            a, b = board.index(0), board.index(0) + 3
            board[b], board[a] = board[a], board[b]
            return board
            
        if move == 'Left':
            a, b = board.index(0), board.index(0) - 1
            board[b], board[a] = board[a], board[b]
            return board
        
        if move == 'Right':
            a, b = board.index(0), board.index(0) + 1
            board[b], board[a] = board[a], board[b]
            return board
        
        else:
            print("not a legal move") 
    
    def getChildren(self):
        # Return a list of boardstates(class)
        # That can be generated from current state  
        children = []
        
        for m in self.getAvailMoves():
            children.append(self.move(m))
        
        return children
    

class Solver(object):
    # Parent class for solvers
    
    def __init__(self,startState):
        # Creates a new solver with start and goal
        self.startState = startState
        self.goalState = [0,1,2,3,4,5,6,7,8]
        self.explored = []
        self.frontier = [self.startState]
        
    def getStart(self):
        # Returns starting state as Board(class)
        return self.startState
    
    def getGoal(self):
        # Returns the goal state as Board(class)
        return self.goalState
        
    def getExplored(self):
        # Returns list of boards(list) that has been explored
        return self.explored
    
    def explore(self,state):
        # Explore a state(Boards): puts it into the explored, check if its goal
        # Return boolean for Succes or Failure
        self.explored.append(state.getBoard())
        
        if state.getBoard() == self.getGoal():
            return True
        else:
            return False
        
    def getFrontier(self):
        # Returns the Boards that is ready to explored
        # The way they are represented may differ for different solvers
        # Start state is automaticly in there
        return self.frontier
        
        
class BFS(Solver):
    # Breadth first search solver
    def __init__(self,StartState):
        # Inits a BFS solver using Solver init.
        Solver.__init__(self,StartState)
        
    def chooseNextBoard(self):
        # Removes last state in queue and returns it
        return self.getFrontier().pop()
    
    def addToFrontier(self,board):
        # Takes a state and puts it in queue, doesnt return anything
        return self.getFrontier().insert(0,board)

    
class DFS(Solver):
    # Depth first search solver
    pass

class AStar(Solver):
    # A* solver
    pass

def runSolver(solverType, startState):
    # The main function that control solver
    # Takes a solver type (BFS, DFS, AStar)
    # Returns some cool stuff ??
    
    #Creates a solver
    solver = solverType(startState)
    
    # Main loop (checks if frontier is empty)
    beginning_time = time.time()
    while len(solver.getFrontier()) != 0:
            
        # Gets new state from queue
        state = Board(solver.chooseNextBoard())
        
        # Explore current state
        if solver.explore(state):
            print("Succes!")
            print("Phew! That took ", str(time.time()-beginning_time))
            return state
        
        # Puts possible children in the frontier
        for c in state.getChildren():
            if not (c in solver.getExplored() and c in solver.getFrontier()):
                solver.addToFrontier(c)
    
    print("Failure!")
    return solver.getExplored()
