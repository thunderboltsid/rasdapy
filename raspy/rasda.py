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


class ExpNode(object):
    """
    A class to represent a node in the expression for the construction of
    query evaluation tree
    """

    def __init__(self, parent=None, value=None, lchild=None, rchild=None, reflected=False, function=False):
        """
        Constructor for the class
        """
        self._parent = parent
        self._lchild = lchild
        self._rchild = rchild
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

    def set_lchild(self, child):
        """
        setter for adding a child to the node
        """
        self._lchild = child

    def set_rchild(self, child):
        """
        setter for adding a child to the node
        """
        self._rchild = child

    def remove_lchild(self):
        """
        delete the left child from node
        """
        self._lchild = None

    def remove_rchild(self):
        """
        delete the right child from node
        """
        self._rchild = None

    @property
    def is_reflected(self):
        """
        A getter for whether the node represents a reflected operation or not
        """
        return self._reflected

    @property
    def is_function(self):
        """
        A getter for whether the node represents a function or not
        """
        return self._function

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
    def lchild(self):
        """
        A getter for the children of the node
        """
        return self._lchild

    @property
    def rchild(self):
        """
        A getter for the children of the node
        """
        return self._rchild


class Filter(object):
    def __init__(self, condition=None):
        self._condition = condition

    def __str__(self):
        return self._condition


class RasCollection(object):
    def __init__(self, name, db=None):
        self._collection = name
        self._condition = None
        self._query = None
        self._leaf = ExpNode(value=name)
        self._root = self._leaf
        self._filters = []
        self._db = None
        self.use_db(db)

    def use_db(self, db):
        if db is not None:
            if isinstance(db, Database):
                self._db = db
            else:
                raise Exception("Argument passed not an instance of ras.Database")

    def eval(self):
        if self._db is not None:
            txn = self._db.transaction()
            query = txn.query(str(self.query))
            data = query.eval()
            txn.abort()
            return data

    def _operation_helper(self, operator, operand, reflected=False, function=False):
        exp = deepcopy(self)
        par = ExpNode(value=operator, reflected=reflected, function=function)
        par.set_rchild(ExpNode(value=operand, parent=par))
        if exp.expression is not None:
            exp._root.set_parent(par)
            par.set_lchild(exp._root)
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
        return self._operation_helper("pow", [other], function=True)

    def __getitem__(self, *args):
        exp = deepcopy(self)
        if len(args) == 0:
            return exp
        if type(args[0]) is tuple:  # If type is tuple
            value = [slice_tuple(arg) for arg in args[0]]
            exp._leaf.set_value(represent_subsetting(exp._leaf.value, value))
        elif type(args[0]) is slice:  # If type is slice
            exp._leaf.set_value(exp._leaf.value + "[" + str(args[0].start) + "," + str(args[0].stop) + "]")
        else:
            exp._leaf.set_value(exp._leaf.value + "[" + str(args[0]) + "]")
        return exp

    def __abs__(self):
        pass

    def exp(self, other):
        return self._operation_helper("exp", [other], function=True)

    def sqrt(self):
        return self._operation_helper("sqrt", [], function=True)

    def log(self):
        pass

    def ln(self):
        pass

    def sin(self):
        pass

    def cos(self):
        pass

    def tan(self):
        pass

    def sinh(self):
        pass

    def cosh(self):
        pass

    def tanh(self):
        pass

    def arcsin(self):
        pass

    def arccos(self):
        pass

    def arctan(self):
        pass

    def avg_cells(self):
        pass

    def sdom(self):
        sdom_q = self._operation_helper("sdom", [], function=True)
        return sdom_q.eval()

    def filter(self, **kwargs):
        for key in kwargs:
            filter = str(key) + "=" + str(kwargs[key])
            self._filters.append(Filter(condition=filter))
        self._condition = " and ".join(str(fltr) for fltr in self._filters)

    @property
    def query(self):
        return RasQuery(collection=self.collection, expression=self.expression, condition=self.condition)

    @property
    def collection(self):
        return self._collection

    @property
    def expression(self):
        temp = self._leaf
        exp = temp.value
        while temp.parent is not None:
            if temp.parent.is_reflected is False and temp.parent.is_function is False:
                exp = "(" + exp + temp.parent.value + str(
                    temp.parent.rchild.value) + ")"
            elif temp.parent.is_function is True and temp.parent.is_reflected is False:
                args = temp.parent.rchild.value
                arg_str = ","
                for arg in args:
                    arg_str += str(arg)
                    arg_str += ","
                if arg_str != ",":
                    arg_str = arg_str[:-1]
                else:
                    arg_str = ""

                exp = temp.parent.value + "(" + exp + arg_str + ")"
            else:
                exp = "(" + str(
                    temp.parent.rchild.value) + temp.parent.value + exp + ")"
            temp = temp.parent
        return exp

    @property
    def condition(self):
        return self._condition


class RasQuery(object):
    def __init__(self, collection=None, expression=None, condition=None):
        self._collection = collection
        self._expression = expression
        self._condition = condition

    def __str__(self):
        if self._condition is not None:
            query_str = "select " + self._expression + " from " + self._collection + " where " + self._condition
        else:
            query_str = "select " + self._expression + " from " + self._collection
        return query_str


col = RasCollection("mr")
col /= 9
col **= 2
col = col[1:10]
col.filter(oid=2)
import pdb; pdb.set_trace()
