import numpy

import problem
import state as S
import property as P
import search as SRCH



N = 20
seed = 42
goal = set(range(N))
initial = ([])
parentState = dict()
stateCost = dict()

props = P.Properties(N, seed, goal, initial)

problem = problem.makeProblem(props.N, props.seed)
# problem = sorted(problem, key=lambda l: len(l))

initialState = S.State(props.initial)
goalState = S.State(props.goal)
# initialState = S.State(numpy.array([1,2,34,3,5]))

def h(currentState : S):
    # return (numpy.sum((currentState != goalState) & (numpy.array(list(currentState.contain()))))).size
    # return numpy.sum( ( currentState != goalState ) & (numpy.array(list(currentState.contain()))))
    return len(currentState.contain())

path = SRCH.doesSearch(initialState, goalState, parentState, stateCost, problem,
                       unitCost= lambda s:1,
                       priorityFunction=lambda s: h(s) / stateCost[s] )
print (path)