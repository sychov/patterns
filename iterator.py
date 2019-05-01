#-----------------------------------------------------------------------------#
# Name:        iterator.py
# Author:      Ryoga
# Created:     20.04.2019
# Description: Iterator (cursor) pattern.
#              Main idea is to separate iterator's and collection's logics
#              in different classes.
#              BTW, I think in Python it is better to use standard iteration
#              protocol, for consinstency. I did this way.
#-----------------------------------------------------------------------------#


import abc


# -------------------- INTERFACES ------------------------- #

class TreeIntegrityError(ValueError):
    """Simple exception, raised when initialization tree value
    is incorrect.
    """
    pass


class Iterable(abc.ABC):
    """Abstract iterator class.
    Declares method '__next__()'
    """
    @abc.abstractmethod
    def __next__(self):
        pass

    def __iter__(self):
        return self


class Collection(abc.ABC):
    """Collection interface.
    Declares method '__iter__()'
    """
    @abc.abstractmethod
    def __iter__(self) -> Iterable:
        pass


# -------------------- ABSTRACT CLASSES ------------------------- #

class Tree(Collection, abc.ABC):
    """Tree abstract class.
    Particular iterator chosen in factory method "__iter__()".
    """
    def __init__(self, tree: dict):
        self._tree = tree
        self._check_integrity()

    @abc.abstractmethod
    def __iter__(self):
        pass

    def _check_integrity(self):
        """Checks integrity of input value.
        """
        try:
            for q in self:
                pass
        except TreeIntegrityError:
            raise ValueError('Invalid "tree" parameter.')


# -------------------- PARTICULAR CLASSES ------------------------- #

class TreeDepthIterator(Iterable):
    """Iterator for tree's "Depth-first iteration".
    """
    def __init__(self, collection: Tree):
        self._collection = collection
        self._cursor = None

    def __next__(self):
        if not self._cursor:
            self._cursor = self._walk(self._collection)
        return next(self._cursor)

    def _walk(self, element):
        """Generator. Recursive algorithm of "Depth-first iteration".
        """
        if not isinstance(element, dict) or len(element) != 1:
            raise TreeIntegrityError
        key, sublist = tuple(element.items())[0]
        if not isinstance(sublist, list):
            raise TreeIntegrityError
        yield key
        for sublist_element in sublist:
            for recursive_elem in self._walk(sublist_element):
                yield recursive_elem


class TreeBreadthIterator(Iterable):
    """Iterator for tree's "Breadth-first iteration".
    """
    def __init__(self, collection: Tree):
        self._collection = collection
        self._slice = None
        self._cursor = None

    def __next__(self):
        if not self._cursor:
            self._slice = [self._collection]
            self._cursor = self._walk()
        return next(self._cursor)

    def _walk(self):
        """Generator. Algorithm of "Breadth-first iteration".
        """
        while self._slice:
            new_slice = []
            for element in self._slice:
                if not isinstance(element, dict) or len(element) != 1:
                    raise TreeIntegrityError
                key, sublist = tuple(element.items())[0]
                if not isinstance(sublist, list):
                    raise TreeIntegrityError
                yield key
                new_slice.extend(sublist)
            self._slice = new_slice


class DTree(Tree):
    """Realization of tree with "deep iteration".
    """
    def __iter__(self):
        return TreeDepthIterator(self._tree)


class WTree(Tree):
    """Realization of tree with "deep iteration".
    """
    def __iter__(self):
        return TreeBreadthIterator(self._tree)


# --------------------------- TEST --------------------------------#

if __name__ == '__main__':
    test_tree = {
        '1': [{'2': [{'12': []}]},
              {'3': []},
              {'4': [{'6': []}, {'7': [{'13': []}]}, {'8': []}]},
              {'5': [{'9': []}, {'10': [{'11': []}]}]}
        ]
    }
    print(' - '.join(DTree(test_tree)))
    print(' - '.join(WTree(test_tree)))



