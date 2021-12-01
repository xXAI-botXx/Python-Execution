from __future__ import annotations
from typing import *
from dataclasses import dataclass
import unittest

@dataclass
class ListEntry:
    data: Any
    next: ListEntry = None

class ImmutableList:
    def __init__(self, first: ListEntry=None):
        self.first = first

    @staticmethod
    def fromPythonList(pyList: List[Any]) -> ImmutableList:
        l = ImmutableList()
        for i in range(len(pyList) - 1, -1, -1):
           l = l.prepend(pyList[i])
        return l

    @property
    def isEmpty(self) -> bool:
        return self.first is None

    def prepend(self, x: Any) -> ImmutableList:
        return ImmutableList(ListEntry(x, self.first))

    @property
    def head(self) -> Any:
        if self.first is None:
            raise ValueError('empty list')
        else:
            return self.first.data

    @property
    def tail(self) -> ImmutableList:
        if self.first is None:
            raise ValueError('empty list')
        else:
            return ImmutableList(self.first.next)

    def asPythonList(self) -> List[Any]:
        res = []
        cur = self.first
        while cur is not None:
            res.append(cur.data)
            cur = cur.next
        return res

    def drop(self, n: int) -> ImmutableList:
        if n <= 0 or self.isEmpty:
            return self
        return self.tail.drop(n-1)


    # schau dir einzelne Fälle an, um es besser nachvollziehen zu können
    def limit(self, n: int) -> ImmutableList:
        if n <= 0 or self.isEmpty:
            return ImmutableList()
        else:
            return self.tail.limit(n-1).prepend(self.head)

    def __repr__(self):
        return f'ImmutableList({self.asPythonList()})'

class ImmutableListTest(unittest.TestCase):

    def testBasics(self):
        l = ImmutableList()
        self.assertTrue(l.isEmpty)
        with self.assertRaises(ValueError):
            l.head
        with self.assertRaises(ValueError):
            l.tail
        self.assertEqual([], l.asPythonList())
        l1 = l.prepend("foo").prepend("bar")
        self.assertEqual(["bar", "foo"], l1.asPythonList())
        self.assertFalse(l1.isEmpty)
        self.assertEqual("bar", l1.head)
        self.assertEqual(["foo"], l1.tail.asPythonList())

    def testFromPythonList(self):
        l = ImmutableList.fromPythonList([1,2,3])
        self.assertEqual([1,2,3], l.asPythonList())

    def assertLimit(self, l, n, expected):
        il = ImmutableList.fromPythonList(l)
        self.assertEqual(expected, il.limit(n).asPythonList())
        self.assertEqual(l, il.asPythonList())
    
    def testLimit(self):
        self.assertLimit([], 2, [])
        self.assertLimit([], -1, [])
        self.assertLimit([1,2,3], 2, [1,2])
        self.assertLimit([1,2,3], 5, [1,2,3])
        self.assertLimit([1,2,3], 0, [])
        self.assertLimit([1,2,3], -1, [])

    def assertDrop(self, l, n, expected):
        il = ImmutableList.fromPythonList(l)
        self.assertEqual(expected, il.drop(n).asPythonList())
        self.assertEqual(l, il.asPythonList())

    def testAssertDrop(self):
        self.assertDrop([], 2, [])
        self.assertDrop([], 0, [])
        self.assertDrop([], -1, [])
        self.assertDrop([1,2,3], 5, [])
        self.assertDrop([1,2,3], 3, [])
        self.assertDrop([1,2,3], 2, [3])
        self.assertDrop([1,2,3], 1, [2,3])
        self.assertDrop([1,2,3], 0, [1,2,3])
        self.assertDrop([1,2,3], -2, [1,2,3])

if __name__ == '__wypp__':
    unittest.main(argv=['ignored'], exit=False)
elif __name__ == '__main__':
    unittest.main()
