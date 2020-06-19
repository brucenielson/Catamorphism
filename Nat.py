from typing import Callable
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


def cataNat(n: Nat, zeroCase: T, succCase: Callable[[T], T] ) -> T:
    if type(n) == Zero:
        return zeroCase
    elif type(n) == Succ:
        return succCase(cataNat(n.pred, zeroCase, succCase))

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