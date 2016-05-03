from copy import deepcopy
from ras import *


class Node:
    def __init__(self, parent=None, value=None, children=[], reflected=False):
        self._parent = parent
        self._children = children
        self._value = value
        self._reflected = reflected

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

    def _operation_helper(self, operator, operand):
        exp = deepcopy(self)
        par = Node(value=operator)
        par.add_child(Node(value=operand, parent=par))
        if exp.expression is not None:
            exp._root.set_parent(par)
            par.add_child(exp._root)
        exp._root = par
        return exp

    def _reflected_operation_helper(self, operator, operand):
        exp = deepcopy(self)
        par = Node(value=operator, reflected=True)
        par.add_child(Node(value=operand, parent=par))
        if exp.expression is not None:
            exp._root.set_parent(par)
            par.add_child(exp._root)
        exp._root = par
        return exp

    def __add__(self, other):
        return self._operation_helper("+", other)

    def __radd__(self, other):
        return self._reflected_operation_helper("+", other)

    def __isub__(self, other):
        return self._operation_helper("-", other)

    def __rsub__(self, other):
        return self._reflected_operation_helper("-", other)


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
            if temp.parent.reflected is False:
                exp = "(" + exp + temp.parent.value + str(temp.parent.children[len(temp.parent.children)-2].value) + ")"
            else:
                exp = "(" +  str(temp.parent.children[len(temp.parent.children)-2].value) + temp.parent.value + exp  + ")"
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
