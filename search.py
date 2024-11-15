# search.py

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    return ['South', 'South', 'West', 'South', 'West', 'West', 'South', 'West']


def __genericSearch__(problem, stack_type):
    if stack_type == 'FIFO':
        stack = util.Queue()
    else:
        stack = util.Stack()

    visited = []
    stack.push((problem.getStartState(), []))

    while not stack.isEmpty():
        node = stack.pop()

        if node[0] not in visited:

            if problem.isGoalState(node[0]):
                return node[1]

            visited.append(node[0])

            for action in problem.getSuccessors(node[0]):
                if action[0] not in visited:
                    stack.push((action[0], (node[1] + [action[1]])))


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    return __genericSearch__(problem, 'LIFO')


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    return __genericSearch__(problem, 'FIFO')


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    stack = util.PriorityQueue()

    visited = []
    stack.push((problem.getStartState(), [], 0), 0)

    while not stack.isEmpty():
        node = stack.pop()

        if node[0] not in visited:

            if problem.isGoalState(node[0]):
                return node[1]

            visited.append(node[0])

            for action in problem.getSuccessors(node[0]):
                if action[0] not in visited:
                    stack.push((action[0], (node[1] + [action[1]]), node[2] + action[2]), node[2] + action[2])


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    stack = util.PriorityQueue()

    visited = []
    stack.push((problem.getStartState(), [], 0), 0)

    while not stack.isEmpty():
        node = stack.pop()

        if node[0] not in visited:

            if problem.isGoalState(node[0]):
                return node[1]

            visited.append(node[0])

            for action in problem.getSuccessors(node[0]):
                if action[0] not in visited:
                    stack.push((action[0], (node[1] + [action[1]]), node[2] + action[2]),
                               node[2] + action[2] + heuristic(action[0], problem))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
