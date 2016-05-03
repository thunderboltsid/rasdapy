from copy import deepcopy
from ras import *


class Node:
    def __init__(self, parent=None, value=None, children=[], reflected=False, function=False):
        self._parent = parent
        self._children = children
        self._value = value
        self._reflected = reflected
        self._function = function

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

    def _operation_helper(self, operator, operand, reflected=False, function=False):
        exp = deepcopy(self)
        if reflected is False and function is False:
            par = Node(value=operator)
        elif reflected is True and function is False:
            par = Node(value=operator, reflected=True)
        else:
            par = Node(value=operator, function=True)
        par.add_child(Node(value=operand, parent=par))
        if exp.expression is not None:
            exp._root.set_parent(par)
            par.add_child(exp._root)
        exp._root = par
        return exp

    def __add__(self, other):
        return self._operation_helper("+", other)

    def __radd__(self, other):
        return self._operation_helper("+", other, reflected=True)

    def __sub__(self, other):
        return self._operation_helper("-", other)

    def __rsub__(self, other):
        return self._operation_helper("-", other, reflected=True)

    def __mul__(self, other):
        return self._operation_helper("*", other)

    def __rmul__(self, other):
        return self._operation_helper("*", other, reflected=True)

    def __div__(self, other):
        return self._operation_helper("/", other)

    def __rdiv__(self, other):
        return self._operation_helper("/", other, reflected=True)

    def __pow__(self, other):
        return self._operation_helper("exp", other, function=True)


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
            if temp.parent._reflected is False and temp.parent._function is False:
                exp = "(" + exp + temp.parent.value + str(temp.parent.children[len(temp.parent.children)-2].value) + ")"
            elif temp.parent._function is True and temp.parent._reflected is False:
                exp = temp.parent.value + "(" + exp + "," + str(temp.parent.children[len(temp.parent.children)-2].value) + ")"
            else:
                exp = "(" +  str(temp.parent.children[len(temp.parent.children)-2].value) + temp.parent.value + exp  + ")"
            temp = temp.parent
        return exp

    @property
    def condition(self):
        return self._condition


class Query:
    def __init__(self, collection, expression, condition):
        if condition is not None:
            self._query_str = "select " + expression + " from " + collection + " where " + condition
        else:
            self._query_str = "select " + expression + " from " + collection

    def __str__(self):
        return self._query_str


col = Coll("mr")
col += 2
col += 5
import pdb; pdb.set_trace()
