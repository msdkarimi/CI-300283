import logging
import priorityQueue as PQ
import state
import problem as PROB
import numpy

def goalStateCheck(stateToBeChecked : state, goal : state):
    return set(stateToBeChecked.contain()) == set(goal.contain())


def resultOfAction(currentState : state, action: numpy.ndarray):
    # temp = currentState.contain()
    # temp.append(action)
    # temp = tuple(temp)
    # return temp

    #
    cS = set(currentState.copyData())
    cS |= set(action)
    return state.State(cS)



def doesSearch ( initialStat: state,
                goal : state,
                parentState : dict,
                stateCost: dict,
                problem : PROB,
                unitCost : callable,
                priorityFunction : callable
                 ):
    # print(len(problem))
    print(problem)
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
          cost = unitCost(p)

          # if type(res) != int:
          #     newState = res
          #     cost = unitCost(p)
          # else:
          #     continue
          # newState = resultOfAction(currentState, p)
          # cost = unitCost(p)
          if newState not in stateCost and newState not in frontier:
               parentState[newState] = currentState
               stateCost[newState] = stateCost[currentState] + cost
               frontier.push(newState, p = priorityFunction(newState, currentState))
               # logging.warning(f"Added new node to frontier (cost={ stateCost[newState]})")
          elif newState in frontier and stateCost[newState] > stateCost[currentState] + cost:
               old_cost = stateCost[currentState]
               parentState[newState] = currentState
               stateCost[newState] = stateCost[currentState] + cost
               # logging.warning(f"Updated node cost in frontier: {old_cost} -> {stateCost[newState]}")

       if frontier:
           currentState = frontier.pop()

       else:
           currentState = None

    path = list()
    s = currentState

    while s:
        path.append(s.copyData())
        s = parentState[s]
        # path.append(s.copyData())

    logging.warning(f"Found a solution in {len(path):,} steps; visited {len(stateCost):,} states")
    return list(reversed(path))


