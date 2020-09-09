# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import game
import time

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
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):

    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
"""
    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """A WHOLE NIGHT FINISHING ONLY THIS FUNCION..."""
    stack=util.Stack()
    stack.push((problem.getStartState(),0))
    checkedStates={}
    checkedStates[problem.getStartState()]=[]
    from game import Directions
    while stack.isEmpty()==False:
        tempState=stack.pop()
        #print("span:"+str(tempState))
        if problem.isGoalState(tempState[0]):
            return checkedStates[tempState[0]]
        successors=problem.getSuccessors(tempState[0])
        # bubble sort according to the cost
        for i in range(len(successors) - 1):
            for j in range(1, len(successors)):
                if (successors[i][2] > successors[j][2]):
                    exchange = successors[i]
                    successors[i] = successors[j]
                    successors[j] = exchange
        #print(successors)
        for i in range(len(successors)):
            nextState = successors[i]
            #print(str(nextState)+"!!!")
            if nextState[0] not in checkedStates.keys():
                stack.push((nextState[0],nextState[1]))
                totalSteps = checkedStates[tempState[0]][:]
                totalSteps.append(nextState[1])
                checkedStates[nextState[0]] = totalSteps
            else:
                totalSteps = checkedStates[tempState[0]][:]
                totalSteps.append(nextState[1])
                checkedStates[nextState[0]] = totalSteps
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()

#-l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
#-l mediumMaze -p SearchAgent -a fn=bfs
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    count=0
    #time.sleep(1000)
    queue = util.Queue()
    queue.push((problem.getStartState(), 0))
    #print(problem.getStartState())
    checkedStates = {}
    checkedStates[problem.getStartState()] = []
    while queue.isEmpty() == False:
        tempState = queue.pop()
        count+=1
        if problem.isGoalState(tempState[0]):
            #print("steps::::"+str(checkedStates[tempState[0]]))
            #print("lenght::::" + str(len(checkedStates[tempState[0]])))
            return checkedStates[tempState[0]]
        successors = problem.getSuccessors(tempState[0])
        # bubble sort according to the cost
        for i in range(len(successors) - 1):
            for j in range(1, len(successors)):
                if (successors[i][2] >= successors[j][2]):
                    exchange = successors[i]
                    successors[i] = successors[j]
                    successors[j] = exchange
        # print(successors)
        for i in range(len(successors)):
            nextState = successors[i]
            if nextState[0] not in checkedStates.keys():
                queue.push((nextState[0], nextState[1]))
                totalSteps = checkedStates[tempState[0]][:]
                totalSteps.append(nextState[1])
                checkedStates[nextState[0]] = totalSteps
    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    pQueue = util.PriorityQueue()#heap, pop out the least number.
    pQueue.push((problem.getStartState(), 0),0) #((state, get here by action:),priority).
    checkedStates = {}
    checkedStates[problem.getStartState()] = [(0,0)]#[(actions , cost from goal),...]
    from game import Directions
    while pQueue.isEmpty() == False:
        tempState = pQueue.pop()
        if problem.isGoalState(tempState[0]):
            #print(checkedStates[tempState[0]])
            steps=checkedStates[tempState[0]]
            result=[]
            for i in range(1,len(steps)):
                result.append(steps[i][0])
            return result#delete the first item
        successors = problem.getSuccessors(tempState[0])
        # bubble sort according to the cost
        for i in range(len(successors)):
            nextState = successors[i]
            # print(str(nextState)+"!!!")
            if nextState[0] not in checkedStates.keys():
                pQueue.push((nextState[0], nextState[1]),checkedStates[tempState[0]][-1][1]+nextState[2])
                totalSteps = checkedStates[tempState[0]][:]
                totalSteps.append((nextState[1],checkedStates[tempState[0]][-1][1]+nextState[2]))
                checkedStates[nextState[0]] = totalSteps
            else:
                costInHeap=checkedStates[nextState[0]][-1][1]
                if costInHeap> checkedStates[tempState[0]][-1][1] + nextState[2]:
                    totalSteps = checkedStates[tempState[0]][:]
                    totalSteps.append((nextState[1], checkedStates[tempState[0]][-1][1] + nextState[2]))
                    checkedStates[nextState[0]] = totalSteps

        #print(pQueue.heap)
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    pQueue = util.PriorityQueue()  # heap, pop out the least number.
    pQueue.push((problem.getStartState(), 0),
                heuristic(problem.getStartState(),problem))  # ((state, get here by action:),priority).
    #print("!!!"+str(heuristic(problem.getStartState(),problem)))
    checkedStates = {}
    checkedStates[problem.getStartState()] = \
        [(0, 0)]  # [(actions , cost),...]
    while pQueue.isEmpty() == False:
        tempState = pQueue.pop()
        if problem.isGoalState(tempState[0]):
            # print(checkedStates[tempState[0]])
            steps = checkedStates[tempState[0]]
            result = []
            for i in range(1, len(steps)):
                result.append(steps[i][0])
            return result  # delete the first item
        successors = problem.getSuccessors(tempState[0])
        for i in range(len(successors)):
            nextState = successors[i]
            if nextState[0] not in checkedStates.keys():
                pQueue.update((nextState[0], nextState[1]), checkedStates[tempState[0]][-1][1] \
                            + nextState[2]+heuristic(nextState[0],problem))
                totalSteps = checkedStates[tempState[0]][:]
                totalSteps.append((nextState[1], checkedStates[tempState[0]][-1][1] \
                                   + nextState[2]))
                checkedStates[nextState[0]] = totalSteps
            else:
                costInHeap = checkedStates[nextState[0]][-1][1]
                #print(str(costInHeap)+"::"+str(checkedStates[tempState[0]][-1][1] + nextState[2]))
                if costInHeap > checkedStates[tempState[0]][-1][1] + nextState[2]:
                    totalSteps = checkedStates[tempState[0]][:]
                    totalSteps.append((nextState[1], checkedStates[tempState[0]][-1][1]
                                       + nextState[2]))
                    checkedStates[nextState[0]] = totalSteps
                    pQueue.update((nextState[0], nextState[1]), checkedStates[nextState[0]][-1][1] \
                                  + heuristic(nextState[0], problem))
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
