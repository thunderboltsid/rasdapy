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
from raspy import ras
from raspy import utils
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
        inp_str = "set<marray<char, [100:140, 40:80]>>"
        self.assertEqual(utils.get_type_structure_from_string(inp_str), {"base_type":"marray", "type":"char"})

    def test_type_structure_struct(self):
        inp_str = "set<marray<struct{short foo, char bar}, [100:150, 50:80]>>"
        self.assertEqual(utils.get_type_structure_from_string(inp_str), {"base_type":"marray", "type":"struct", "sub_type":("short", "char")})

    def test_convert_data_from_bin(self):
        test_inp = [{"dtype":"char", "data":"\x16"}]
        test_out = [21]
        if len(test_inp) == len(test_out):
            for i in xrange(0,len(test_inp)-1):
                self.assertEqual(utils.convert_data_from_bin(test_inp[i]["dtype"], test_inp[i]["data"]))


class TestConnectionDefault(unittest.TestCase):
    def setUp(self):
        self.connection = ras.Connection()

    def test_disconnect_connection(self):
        self.connection.disconnect()

    def test_reconnect_connection(self):
        self.connection.connect()

    def test_connect_default_settings(self):
        self.assertEqual(self.connection.hostname, "0.0.0.0")
        self.assertEqual(self.connection.port, 7001)
        self.assertEqual(self.connection.username, "rasguest")
        self.assertEquals(self.connection.password, "rasguest")


# class TestConnectionCustom(unittest.TestCase):
#     def setUp(self):
#         self.connection = ras.Connection(hostname="192.168.1.1", port=50051, username="testuser", password="dJ4ng0Pi5")
#
#     def test_disconnect_connection(self):
#         self.connection.disconnect()
#
#     def test_reconnect_connection(self):
#         self.connection.connect()
#
#     def test_connect_custom_settings(self):
#         self.assertEqual(self.connection.hostname, "192.168.1.1")
#         self.assertEqual(self.connection.port, 7000)
#         self.assertEqual(self.connection.username, "testuser")
#         self.assertEquals(self.connection.password, "dJ4ng0Pi5")


if __name__ == "__main__":
    unittest.main()


