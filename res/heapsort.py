from __future__ import annotations

def heapifyFull(seq: Sequence):
    heapify(0, seq, len(seq)-1)

def heapify(i: int, seq: Sequence, right: int):
    """
    heapify(i, seq, n) lässt das Element am Index i im Heap versickern.
    Der Heap ist als Sequenz seq repräsentiert. right gibt den Index des
    letzten Elements aus seq an, welches noch zum Heap gehört.
    SEITENEFFEKT: seq wird in place geändert.
    """
    # get left child
    if 2*i+1 > right:
        elem_l = None
    else:
        elem_l = seq[2*i+1]

    # get right child
    if 2*i+2 > right:
        elem_r = None
    else:
        elem_r = seq[2*i+2]

    # how many children did we have? -> check childs
    if elem_l == None and elem_r == None:
        return None
    elif not(elem_l == None) and not(elem_r == None):
        # get bigger element
        if elem_l > elem_r:
            elem = elem_l
            elem_i = 2*i+1
        else:
            elem = elem_r
            elem_i = 2*i+2
    elif not(elem_l == None) and elem_r == None:
        elem = elem_l
        elem_i = 2*i+1
    elif elem_l == None and not(elem_r == None):
        elem = elem_r
        elem_i = 2*i+2

    # compare bigger one with your sinking value
    if seq[i] < elem:
        seq[elem_i], seq[i] = seq[i], seq[elem_i]
        i = elem_i
        heapify(i, seq, right)
    else:
        pass

def sort(seq: Sequence):
    n = len(seq)
    # Generiere Max-Heap Form
    for i in range(n//2, -1, -1):
        heapify(i, seq, n-1)
    # Wiederhole: 1. Verschieben + 2. Versickern
    for i in range(n-1, -1, -1):  # bis 0 ginge auch
        heapify(0, seq, i)
        seq[0], seq[i] = seq[i], seq[0]

def swap(seq, i, j):
    x = seq[i]
    seq[i] = seq[j]
    seq[j] = x

import SortTest
import unittest

class HeapSortTest(SortTest.SortTest):
    def testHeapSort(self):
        self.allTestsForSortAlgorithm(sort)

    def testHeapify1(self):
        l = []
        heapifyFull(l)
        self.assertEqual(l, [])

    def testHeapify2(self):
        l = [1,2,3]
        heapifyFull(l)
        self.assertEqual(l, [3,2,1])

    def testHeapify3(self):
        l = [1,3,2]
        heapifyFull(l)
        self.assertEqual(l, [3,1,2])

    def testHeapify4(self):
        l = [3,2,1]
        heapifyFull(l)
        self.assertEqual(l, [3,2,1])

    def testHeapify5(self):
        l = [3,1,2]
        heapifyFull(l)
        self.assertEqual(l, [3,1,2])

    def testHeapify6(self):
        l = [15,43,17,2,40,8]
        heapifyFull(l)
        self.assertEqual(l, [43,40,17,2,15,8])

    def testHeapify7(self):
        l = [0,15,1,43,17,6,7,2,40,8,101]
        heapify(1, l, 8)
        self.assertEqual(l, [0,43,1,40,17,6,7,2,15,8,101])

if __name__ == '__wypp__':
    unittest.main(argv=['ignored'], exit=False)
elif __name__ == '__main__':
    unittest.main()
