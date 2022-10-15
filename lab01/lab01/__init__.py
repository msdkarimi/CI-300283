import problem
import state as S
import property as P
import search

N = 6
seed = 42
goal = set(range(6))
initial = []

props = P.Properties(N, seed, goal, initial)

problem = problem.makeProblem(props.N, props.seed)

initialState = S.State(props.initial)
goalState = S.State(props.goal)

print(initialState)


# result = search.doesSearch()