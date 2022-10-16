import numpy
import problem
import state as S
import property as P
import search as SRCH



N = 5
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

def h(newState : S , currentState : S ):
    # return (numpy.sum((currentState != goalState) & (numpy.array(list(currentState.contain()))))).size
    # return numpy.sum( ( currentState != goalState ) & (numpy.array(list(currentState.contain()))))
    # return len(currentState.contain())
    #
    _cS = currentState.copyData()
    _nS = newState.copyData()
    _cS = set(_cS)
    _nS = set(_nS)
    # _cS |= set(_nS)
    _cS &= set(_nS)
    return len (_cS)

path = SRCH.doesSearch(initialState, goalState, parentState, stateCost, problem,
                       unitCost= lambda s:1,
                       priorityFunction=lambda nS,cS : h(nS , cS) )
W = 0
for p in path:
    W += len(p)
print (path)
print(W)