from typing import Callable
# https://kite.com/python/docs/typing.TypeVar
from typing import TypeVar
# Setup generic type
T = TypeVar('T')

class Nat:
    pass

class Zero(Nat):
    pass

class Succ(Nat):
    def __init__(self, pred: Nat):
        self.pred = pred


# mkNat and getval to test out Nat classes
def mkNat(n: int) -> Nat:
    assert n >= 0
    nat = Zero()
    while n > 0:
        nat = Succ(nat)
        n -= 1
    return nat

def getval(n: Nat) -> int:
    if type(n) == Zero:
        return 0
    else:
        return 1 + getval(n.pred)


n = mkNat(3)
assert getval(n) == 3


# Now attempt to do this via a catamorphism
def cataNat(n: Nat, zeroCase: T, succCase: Callable[[T], T] ) -> T:
    if type(n) == Zero:
        return zeroCase
    elif type(n) == Succ:
        return succCase(cataNat(n.pred, zeroCase, succCase))

def successor(n: Nat) -> Nat:
    return Succ(n)

# Test cataNat on n
n2 = cataNat(n, Zero(), successor)
assert getval(n2) == 3
