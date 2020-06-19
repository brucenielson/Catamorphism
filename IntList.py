from __future__ import annotations
from typing import Callable

class IntList:
    def __init__(self, x: int, xs: IntList):
        self.x = x
        self.xs = xs

    def lenIntList(self):
        if self.x == None:
            return 0
        elif self.xs == None:
            return 1
        else:
            return 1 + self.xs.lenIntList()

    def sumIntList(self):
        if self.x == None:
            return 0
        elif self.xs == None:
            return self.x
        else:
            return self.x + self.xs.sumIntList()

    def __str__(self):
        x = self.x
        xs = self.xs
        if x is None:
            x = "None"
        if xs is None:
            xs = "None"
        return "x: " + str(x) + " - " + self.xs.__str__()


# foldList :: IntList -> Int -> (ConsCase -> Int -> Int) -> Int
# foldList Nil acc _ = acc
# foldList (Cons xs) acc f = f (ConsType (consCaseHead xs) Nil) (foldList (consCaseTail xs) acc f)
def foldList(cons: IntList, acc: int, consCase: Callable) -> int:
    if cons.x is None:
        return acc
    else:
        param1 = IntList(cons.x, None)
        param2 = foldList(cons.xs, acc, consCase)
        print("param1: ", param1)
        print("param2: ", param2)
        return consCase(param1, param2)

# lenConsCase :: ConsCase -> Int -> Int
# lenConsCase _ acc = 1 + acc
# sumConsCase :: ConsCase -> Int -> Int
# sumConsCase cons acc = consCaseHead cons + acc
def lenConsCase(cons: IntList, acc: int) -> int:
    return 1 + acc

def sumConsCase(cons: IntList, acc: int) -> int:
    return cons.x + acc

def mkIntList(lst: list) -> IntList:
    l = len(lst)
    if l == 1:
        return IntList(lst[0], IntList(None, None))
    else:
        x = lst[0]
        xs = lst[1:]
        return IntList(x, mkIntList(xs))


lst = mkIntList([1,2,3])