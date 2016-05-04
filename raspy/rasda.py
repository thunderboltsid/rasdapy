"""
 *
 * This file is part of rasdaman community.
 *
 * Rasdaman community is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * Rasdaman community is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU  General Public License for more details.
 *
 * You should have received a copy of the GNU  General Public License
 * along with rasdaman community.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Copyright 2003 - 2016 Peter Baumann / rasdaman GmbH.
 *
 * For more information please see <http://www.rasdaman.org>
 * or contact Peter Baumann via <baumann@rasdaman.com>.
 *
"""

"""
This module contains the necessary classes and methods for query construction
and evaluation using the rasdapy library via monkey patching (i.e. overloading)
the python magic methods for certain operations.
"""

from copy import deepcopy
from ras import *


class Node:
    """
    A class to represent a node in the expression for the construction of
    query evaluation tree
    """
    def __init__(self, parent=None, value=None, children=[], reflected=False, function=False):
        """
        Constructor for the class
        """
        self._parent = parent
        self._children = children
        self._value = value
        self._reflected = reflected
        self._function = function

    def set_parent(self, parent):
        """
        setter for the parent of the node
        """
        self._parent = parent

    def set_value(self, value):
        """
        setter for the value of the node
        """
        self._value = value

    def add_child(self, child):
        """
        setter for adding a child to the node
        """
        self._children.append(child)

    @property
    def parent(self):
        """
        A getter for the parent of the node
        """
        return self._parent

    @property
    def value(self):
        """
        A getter for the  value of the node
        """
        return self._value

    @property
    def children(self):
        """
        A getter for the children of the node
        """
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

    def __getitem__(self, *args):
        return args
    @property
    def sdom(self):
        """
        Evaluates the SpatialDomain of the expression
        """
        pass

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
