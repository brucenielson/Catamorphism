from typing import Callable
# https://kite.com/python/docs/typing.TypeVar
from typing import TypeVar
# Setup generic type
T = TypeVar('T')

class Nat:
    def __str__(self):
        return str(self.getVal())

    def getVal(self) -> int:
        if type(self) == Zero:
            return 0
        else:
            return 1 + self.pred.getVal()


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

# def getval(n: Nat) -> int:
#     if type(n) == Zero:
#         return 0
#     else:
#         return 1 + getval(n.pred)


# Test Nat classes
n = mkNat(3)
assert n.getVal() == 3
z = mkNat(0)
assert z.getVal() == 0

# Create catamorphism
def cataNat(n: Nat, zeroCase: T, succCase: Callable[[T], T] ) -> T:
    if type(n) == Zero:
        return zeroCase
    elif type(n) == Succ:
        return succCase(cataNat(n.pred, zeroCase, succCase))

# Just a basic successor function -- the end result is that it just copies the Nat -- not very useful. I feel I'm missing something.
def successor(n: Nat) -> Nat:
    return Succ(n)

# Test cataNat on n using successor
n2 = cataNat(n, Zero(), successor)
assert n2.getVal() == 3


# My first attempt to work out how multiplication with Nat would work
# Test cataNat doing some multiplication (this is more than a bit forced)
def mult3(n: Nat) -> Nat:
    return mkNat(n.getVal() + 3)

# Test cataNat on n
n2 = cataNat(n, Zero(), mult3)
print(n2)
assert n2.getVal() == 9
