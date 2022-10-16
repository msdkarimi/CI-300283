import logging
import priorityQueue as PQ
import state
import problem as PROB
import numpy

def goalStateCheck(stateToBeChecked : state, goal : state):

    return set(stateToBeChecked.contain()) == set(goal.contain())

    # if len(stateToBeChecked.contain()) > 0:
    #     result = set (numpy.hstack(numpy.array(list(stateToBeChecked.contain()))))
    #     sortedStateToBeChecked = sorted(result)
    #     return sortedStateToBeChecked == goal.contain()
    # else:
    #     return False

def resultOfAction(currentState : state, action: numpy.ndarray):
    cS = set(currentState.contain())
    cS |= set(action)
    return  state.State(cS)


def doesSearch ( initialStat: state,
                goal : state,
                parentState : dict,
                stateCost: dict,
                problem : PROB,
                unitCost : callable,
                priorityFunction : callable
                 ):
    # print(len(problem))
    # print(problem)
    frontier = PQ.PriorityQueue()
    parentState.clear()
    stateCost.clear()

    currentState = initialStat
    parentState[currentState] = None
    stateCost[currentState] = 0

    print("spanning tree")
    while currentState is not None and not goalStateCheck(currentState, goal):
       for p in problem:
           newState = resultOfAction(currentState, p)
           # newState = state.State(p)
           cost = unitCost(p)

           if newState not in stateCost and newState not in frontier:
               parentState[newState] = currentState
               stateCost[newState] = stateCost[currentState] + cost
               frontier.push(newState, p = priorityFunction(newState))
               # logging.warning(f"Added new node to frontier (cost={ stateCost[newState]})")
           elif newState in frontier and stateCost[newState] > stateCost[currentState] + cost:
               old_cost = stateCost[currentState]
               parentState[newState] = currentState
               stateCost[newState] = stateCost[currentState] + cost
               # logging.warning(f"Updated node cost in frontier: {old_cost} -> {stateCost[newState]}")

       if frontier:
           currentState = frontier.pop()
           # listOfPriorities.append(currentState)

           # currentState = state.State(listOfPriorities.append(popped))
           # currentState = state.State(listOfPriorities.append([99]))

       else:
           currentState = None

    path = list()
    s = currentState

    while s:
        path.append(s.copy_data())
        s = parentState[s]

    logging.warning(f"Found a solution in {len(path):,} steps; visited {len(stateCost):,} states")
    return list(reversed(path))


