#!/usr/bin/env python
"""
    Simple huffman coding implementation for university course.
    @author Daniel Rahier <daniel@rahier.biz>
    @date   November 2012

    Solution derived from
    http://en.literateprograms.org/Huffman_coding_%28Python%29

    Tested with Python 2.7.3. This will not work with Python 3.3.0!
    The priority queue implementation of Python 3 does not allow to push
    items with the same ordering anymore. For this to work we need to write
    comparison operators for the tuples or use a different data structure.
"""
import heapq
import os
import sys


class Huffman(object):
    """Huffman-coded binary tree, created from given text."""

    def __init__(self, text):
        self.fbyc = dict() # Frequency of characters
        self.tree = None # Stores resulting BTree
        self.char_freq(text)
        self.make_tree()

    def char_freq(self, text):
        """Fills self.fbyc with frequency of every character in text."""
        for c in text:
            if c in list(self.fbyc.keys()):
                self.fbyc[c] += 1
            else:
                self.fbyc[c] = 1

    def make_tree(self):
        """Creates huffman binary tree from pairs in cf."""

        # create priority queue of (freq, char) pairs
        pq = [(v, k) for k, v in list(self.fbyc.items())]
        heapq.heapify(pq)

        while len(pq) > 1:
            # get the pairs with the minimal frequency
            r, l = heapq.heappop(pq), heapq.heappop(pq)
            # create new tree node with combined frequency
            p = (l[0] + r[0], l, r)
            heapq.heappush(pq, p)

        self.tree = pq[0]

    def print_codes(self, tree=None, pfx=''):
        """Traverses tree and prints binary representation of all chars."""
        if tree is None: # ugly
            tree=self.tree

        if len(tree) == 2: # found actual (freq, char) pair
            print("%s: %s" % (tree[1], pfx))
        else: # found "middle-node" (freq, left, right)
            self.print_codes(tree[1], pfx + '0')
            self.print_codes(tree[2], pfx + '1')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Specify string or text file as parameter!")
        sys.exit(-1)

    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as f:
            text = f.read().strip()
    else:
        text = sys.argv[1].strip()

    huff = Huffman(text)
    huff.print_codes()
