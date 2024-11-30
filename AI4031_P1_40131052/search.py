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
from game import Directions
from typing import List

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




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
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
    frontier = util.Stack()
    visited = set()
    
    # Push the start state
    frontier.push((problem.getStartState(), [])) # empty path 
    
    while not frontier.isEmpty():
        state, path= frontier.pop()
        
        # Skip already visited states
        if state in visited:
            continue
        visited.add(state)
        
        # Check if we've reached the goal
        if problem.isGoalState(state):
            return path  # Return the list of actions
        
        # Add successors to the stack
        children = problem.getSuccessors(state)
        for next_state, action, _ in children:
            if next_state not in visited:
                frontier.push((next_state, path + [action]))
    
    return []  # Return empty list if no solution is found

    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    frontier = util.Queue()
    visited = set()
    
    # Push the start state
    frontier.push((problem.getStartState(), [])) # empty path 
    
    while not frontier.isEmpty():
        state, path= frontier.pop()
        
        # Skip already visited states
        if state in visited:
            continue
        visited.add(state)
        
        # Check if we've reached the goal
        if problem.isGoalState(state):
            return path  # Return the list of actions
        
        # Add successors to the stack
        children = problem.getSuccessors(state)
        for next_state, action, _ in children:
            if next_state not in visited:
                frontier.push((next_state, path + [action]))
    
    return []  # Return empty list if no solution is found
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    frontier = util.PriorityQueue()
    visited = set()
    start_state = problem.getStartState()
    # Push the start state
    frontier.push((start_state, []), 0) # empty path/ zero sum of costs-> item = (state, path)
    
    while not frontier.isEmpty():
        state, path= frontier.pop()
        costs_until_here = problem.getCostOfActions(path)
        # Skip already visited states
        if state in visited:
            continue
        visited.add(state)
        
        # Check if we've reached the goal
        if problem.isGoalState(state):
            return path  # Return the list of actions
        
        # Add successors to the stack
        children = problem.getSuccessors(state)
        for next_state, action, action_cost in children:
            if next_state not in visited:
                frontier.push((next_state, path + [action]), costs_until_here + action_cost)
    
    return []  # Return empty list if no solution is found
    util.raiseNotDefined()

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    frontier = util.PriorityQueue()
    visited = {}
    start_state = problem.getStartState()
    # Push the start state
    # empty path/ zero sum of costs and heuristic-> item = (state, path, costs_until_here) , 
    frontier.push((start_state, []), 0 + heuristic(start_state, problem)) 
    
    while not frontier.isEmpty():
        state, path= frontier.pop()
        costs_until_here = problem.getCostOfActions(path)
        
        # Check if we've reached the goal
        if problem.isGoalState(state):
            return path  # Return the list of actions

        if state not in visited or visited[state] > costs_until_here:
            visited[state] = costs_until_here
            # Add successors to the stack
            children = problem.getSuccessors(state)
            for next_state, action, action_cost in children:
                frontier.push((next_state, path + [action]),
                                costs_until_here + action_cost + heuristic(next_state, problem))
        
    return []  # Return empty list if no solution is found
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch