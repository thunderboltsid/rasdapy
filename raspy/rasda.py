from copy import deepcopy
from ras import *


class Node:
    def __init__(self, parent=None, value=None, children=[]):
        self._parent = parent
        self._children = children
        self._value = value

    def set_parent(self, parent):
        self._parent = parent

    def set_value(self, value):
        self._value = value

    def add_child(self, child):
        self._children.append(child)

    @property
    def parent(self):
        return self._parent

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children


class Coll:
    def __init__(self, name):
        self._collection = name
        self._condition = None
        self._query = None
        self._leaf = Node(value=name)
        self._root = self._leaf

    def __operation_helper(operator, value):
        exp = deepcopy(self)
        par = Node(value=operator)
        par.add_child(Node(value=value, parent=par))
        if exp.expression is not None:
            exp._root.set_parent(par)
            par.add_child(exp._root)
        exp._root.set_parent(par)
        return exp

    def __add__(self, other):
        return __operation_helper("+", other)


    @property
    def query(self):
        return Query(self.collection, self.expression, self.condition)

    @property
    def collection(self):
        return self._collection

    @property
    def expression(self):
        temp = self._leaf
        exp = self.collection
        while temp.parent is not None:
            exp = "(" + exp + temp.parent.value + str(temp.parent.children[len(temp.parent.children)-2].value) + ")"
            temp = temp.parent
        return exp

    @property
    def condition(self):
        return self._condition


class Query:
    def __init__(self, collection, expression, condition):
        if not condition:
            self._query_str = "select " + expression + " from " + collection + " where " + condition
        else:
            self._query_str = "select " + expression + " from " + collection

    def __str__(self):
        return self._query_str


col = Coll("mr")
col += 2
col += 5
import pdb; pdb.set_trace()
