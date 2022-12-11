from Nim import MyNim
from RowObjectsPair import RowObjectsPair
from copy import deepcopy
x = MyNim(3, 1)
s0 = (0,1)
r0, o0 = s0
srtgy0 = RowObjectsPair(r0, o0)
# 3.1 & 3.2
# MyNim.doNimming(x,{"p":0.61})
# --------------------------------------------------
print(x.inferedStatus["possible_moves"])
# 3.3
state0 =deepcopy( x._rows )
# x.inferedStatus["possible_moves"]-= {s0}
state1 = x.staticNimming(x._rows, srtgy0)
print(x.minMax(state0, state1))






