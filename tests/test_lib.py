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
from rasdapy import utils
from rasdapy.surface import ExpNode, RasCollection
import unittest


class TestUtils(unittest.TestCase):
    def test_md5_hash(self):
        pass_array = ["rasguest", "dJ4ng0Pi5", "m0n4L154", "514cK8oT"]
        hash_array = ["8e70a429be359b6dace8b5b2500dedb0", "a4187b53523c7a13a5dcd3354418f7c7",
                      "a69d024049be4503e206d4f39b54ea2e", "1cecd6d9eebf70df02411d50e45c178f"]
        for index, password in enumerate(pass_array):
            password_hash = utils.get_md5_string(password)
            self.assertEquals(password_hash, hash_array[index])

    def test_type_structure_char(self):
        inp_str = "set <marray <char, [100:140, 40:80]>>"
        self.assertEqual(utils.get_type_structure_from_string(inp_str), {"base_type": "marray", "type": "char"})

    def test_type_structure_struct(self):
        inp_str = "set <marray <struct { short foo, char bar }, [100:150, 50:80]>>"
        self.assertEqual(utils.get_type_structure_from_string(inp_str),
                         {"base_type": "marray", "type": "struct",
                          "sub_type": {"names": ["foo", "bar"], "types": ["short", "char"]}})

    def test_convert_data_from_bin(self):
        test_inp = [{"dtype": "char", "data": "\x16"}]
        test_out = [21]
        if len(test_inp) == len(test_out):
            for i in xrange(0, len(test_inp) - 1):
                self.assertEqual(utils.convert_data_from_bin(test_inp[i]["dtype"], test_inp[i]["data"]), test_out[i])


class TestExpNode(unittest.TestCase):
    def setUp(self):
        self.value = "+"
        self.lchild = "mr"
        self.rchild = "5"

    def test_exp_node_creation(self):
        node = ExpNode(value=self.value, lchild=self.lchild, rchild=self.rchild)
        self.assertEqual(node.value, self.value)
        self.assertEqual(node.lchild, self.lchild)
        self.assertEqual(node.rchild, self.rchild)


class TestQueryConstruction(unittest.TestCase):
    def setUp(self):
        self.query_simple = "select mr from mr"
        self.query_avg_with_subsetting = "select avg_cells(mr[1:10]) from mr"
        self.query_subsetting_with_condition = "select mr[1:10] from mr where oid=2"
        self.query_arithmetic_operations = "select pow(((((mr+9)/2)-3)*5),2) from mr"
        self.query_trigonometric_operations = "select tan(cos(sin(mr))) from mr"

    def test_query_simple(self):
        col = RasCollection("mr")
        self.assertEqual(self.query_simple, str(col.query))

    def test_query_avg_with_subsetting(self):
        col = RasCollection("mr")
        col = col[1:10]
        col = col.avg_cells()
        self.assertEqual(self.query_avg_with_subsetting, str(col.query))

    def test_query_subsetting_with_condition(self):
        col = RasCollection("mr")
        col = col[1:10]
        col.filter(oid=2)
        self.assertEqual(self.query_subsetting_with_condition, str(col.query))

    def test_query_arithmetic_operations(self):
        col = RasCollection("mr")
        col += 9
        col /= 2
        col -= 3
        col *= 5
        col **= 2
        self.assertEqual(self.query_arithmetic_operations, str(col.query))

    def test_query_trigonometric_operations(self):
        col = RasCollection("mr")
        col = col.sin()
        col = col.cos()
        col = col.tan()
        self.assertEqual(self.query_trigonometric_operations, str(col.query))

    def test_query_equal(self):
        col_1 = RasCollection("mr")
        col_1 += 9
        col_1 = col_1[1:10]
        col_1 **= 2
        col_2 = RasCollection("mr")
        col_2 += 9
        col_2 = col_2[1:10]
        col_2 **= 2
        self.assertTrue(col_1 == col_2)


if __name__ == "__main__":
    unittest.main()
