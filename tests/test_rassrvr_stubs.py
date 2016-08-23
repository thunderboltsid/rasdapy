from lib.utils import get_md5_string
from lib.request_factories import make_rassrvr_end_transfer_req, make_rassrvr_abort_transaction_req, \
    make_rassrvr_begin_transaction_req, make_rassrvr_close_db_req, make_rassrvr_commit_transaction_req, \
    make_rassrvr_execute_http_query_req, make_rassrvr_execute_query_req, \
    make_rassrvr_get_next_mdd_req, make_rassrvr_get_next_tile_req, make_rassrvr_keep_alive_req, \
    make_rassrvr_open_db_req, make_rassrvr_create_db_req, make_rassrvr_destroy_db_req, \
    make_rassrvr_is_transaction_open_req, make_rassrvr_start_insert_mdd, make_rassrvr_start_insert_trans_mdd, \
    make_rassrvr_insert_tile_req, make_rassrvr_end_insert_mdd_req, make_rassrvr_insert_collection_req, \
    make_rassrvr_delete_collection_by_name_req, make_rassrvr_delete_collection_by_id_req, \
    make_rassrvr_get_collection_by_name_or_id_req, make_rassrvr_remove_object_from_collection_req, \
    make_rassrvr_get_collection_oids_by_name_or_id, make_rassrvr_init_update_req, make_rassrvr_get_next_element_req, \
    make_rassrvr_execute_update_query_req, make_rassrvr_execute_insert_query_req, make_rassrvr_get_new_oid_req, \
    make_rassrvr_get_object_type_req, make_rassrvr_get_type_structure_req, make_rassrvr_set_format_req, \
    make_rassrvr_begin_streamed_http_query_req, make_rassrvr_get_next_streamed_http_query_req
import unittest


class RasmgrRequestCreationTest(unittest.TestCase):
    def setUp(self):
        self.username = "rasguest"
        self.password = get_md5_string("rasguest")
        self.clientUUID = "loksa-321mlk-sdfklsm-321"
        self.clientId = 6660
        self.dbname = "RASBASE"
        self.dbsid = "ras_786"
        self.rw = True
        self.query = "select mr[100:140, 40:80] from mr"
        self.data = bytes('\xac')
        self.data_length = 1
        self.collName = "mr"
        self.colid = "mr-0613"
        self.domain = bytes("[100:140, 40:80]")
        self.type_len = 12
        self.type_name = "tmp"
        self.type_type = 1
        self.persistence = False
        self.current_format = 16
        self.storage_format = 16
        self.is_name = True
        self.object_type = 1
        self.format = 1
        self.format_params = "{char, char, char}"
        self.transfer_format = 1

    def test_opendb(self):
        req = make_rassrvr_open_db_req(self.clientId, self.dbname)
        self.assertEqual(req.client_id, self.clientId)
        self.assertEqual(req.database_name, self.dbname)

    def test_closedb(self):
        req = make_rassrvr_close_db_req(self.clientId)
        self.assertEqual(req.client_id, self.clientId)

    def test_createdb(self):
        req = make_rassrvr_create_db_req(self.clientId, self.dbname)
        self.assertEqual(req.client_id, self.clientId)
        self.assertEqual(req.database_name, self.dbname)

    def test_destroydb(self):
        req = make_rassrvr_destroy_db_req(self.clientId, self.dbname)
        self.assertEqual(req.client_id, self.clientId)
        self.assertEqual(req.database_name, self.dbname)

    def test_begin_transaction(self):
        req = make_rassrvr_begin_transaction_req(self.clientId, self.rw)
        self.assertEqual(req.client_id, self.clientId)
        self.assertEqual(req.rw, self.rw)

    def test_commit_transaction(self):
        req = make_rassrvr_commit_transaction_req(self.clientId)
        self.assertEqual(req.client_id, self.clientId)

    def test_abort_transaction(self):
        req = make_rassrvr_abort_transaction_req(self.clientId)
        self.assertEqual(req.client_id, self.clientId)

    def test_transaction_open(self):
        req = make_rassrvr_is_transaction_open_req(self.clientId)
        self.assertEqual(req.client_id, self.clientId)

    def test_start_insert_mdd(self):
        req = make_rassrvr_start_insert_mdd(self.clientId, self.collName, self.domain, self.type_len, self.type_name,
                                            self.colid)
        self.assertEqual(req.client_id, self.clientId)
        self.assertEqual(req.collName, self.collName)
        self.assertEqual(req.domain, self.domain)
        self.assertEqual(req.type_length, self.type_len)
        self.assertEqual(req.type_name, self.type_name)
        self.assertEqual(req.oid, self.colid)

    def test_start_insert_trans_mdd(self):
        req = make_rassrvr_start_insert_trans_mdd(self.clientId, self.domain, self.type_len, self.type_name)
        self.assertEqual(req.client_id, self.clientId)
        self.assertEqual(req.domain, self.domain)
        self.assertEqual(req.type_length, self.type_len)
        self.assertEqual(req.type_name, self.type_name)

    def test_insert_tile(self):
        req = make_rassrvr_insert_tile_req(self.clientId, self.persistence, self.domain, self.type_len,
                                           self.current_format, self.storage_format, self.data, self.data_length)
        self.assertEqual(req.client_id, self.clientId)
        self.assertEqual(req.persistent, self.persistence)
        self.assertEqual(req.domain, self.domain)
        self.assertEqual(req.type_length, self.type_len)
        self.assertEqual(req.current_format, self.current_format)
        self.assertEqual(req.storage_format, self.storage_format)
        self.assertEqual(req.data, self.data)
        self.assertEqual(req.data_length, self.data_length)

    def test_end_insert_mdd(self):
        req = make_rassrvr_end_insert_mdd_req(self.clientId, self.persistence)
        self.assertEqual(req.client_id, self.clientId)
        self.assertEqual(req.persistent, self.persistence)

    def test_insert_collection(self):
        req = make_rassrvr_insert_collection_req(self.clientId, self.collName, self.type_name, self.colid)
        self.assertEqual(req.client_id, self.clientId)
        self.assertEqual(req.collection_name, self.collName)
        self.assertEqual(req.type_name, self.type_name)
        self.assertEqual(req.oid, self.colid)

    def test_delete_collection_by_name(self):
        req = make_rassrvr_delete_collection_by_name_req(self.clientId, self.collName)
        self.assertEqual(req.client_id, self.clientId)
        self.assertEqual(req.collection_name, self.collName)

    def test_delete_collection_by_id(self):
        req = make_rassrvr_delete_collection_by_id_req(self.clientId, self.colid)
        self.assertEqual(req.client_id, self.clientId)
        self.assertEqual(req.oid, self.colid)

    def test_remove_object_from_collection(self):
        req = make_rassrvr_remove_object_from_collection_req(self.clientId, self.collName, self.colid)
        self.assertEqual(req.client_id, self.clientId)
        self.assertEqual(req.collection_name, self.collName)
        self.assertEqual(req.oid, self.colid)

    def test_get_collection_by_name_or_id(self):
        req = make_rassrvr_get_collection_by_name_or_id_req(self.clientId, self.colid, self.is_name)
        self.assertEqual(req.client_id, self.clientId)
        self.assertEqual(req.collection_identifier, self.colid)
        self.assertEqual(req.is_name, self.is_name)

    def test_get_collection_oids_by_name_or_id(self):
        req = make_rassrvr_get_collection_oids_by_name_or_id(self.clientId, self.colid, self.is_name)
        self.assertEqual(req.client_id, self.clientId)
        self.assertEqual(req.collection_identifier, self.colid)
        self.assertEqual(req.is_name, self.is_name)

    def test_get_next_mdd(self):
        req = make_rassrvr_get_next_mdd_req(self.clientId)
        self.assertEqual(req.client_id, self.clientId)

    def test_get_next_tile(self):
        req = make_rassrvr_get_next_tile_req(self.clientId)
        self.assertEqual(req.client_id, self.clientId)

    def test_end_transfer(self):
        req = make_rassrvr_end_transfer_req(self.clientId)
        self.assertEqual(req.client_id, self.clientId)

    def test_init_update(self):
        req = make_rassrvr_init_update_req(self.clientId)
        self.assertEqual(req.client_id, self.clientId)

    def test_execute_query(self):
        req = make_rassrvr_execute_query_req(self.clientId, self.query)
        self.assertEqual(req.client_id, self.clientId)
        self.assertEqual(req.query, self.query)

    def test_execute_http_query(self):
        req = make_rassrvr_execute_http_query_req(self.clientId, self.data)
        self.assertEqual(req.client_id, self.clientId)
        self.assertEqual(req.data, self.data)

    def test_get_next_element(self):
        req = make_rassrvr_get_next_element_req(self.clientId)
        self.assertEqual(req.client_id, self.clientId)

    def test_execute_update_query(self):
        req = make_rassrvr_execute_update_query_req(self.clientId, self.query)
        self.assertEqual(req.client_id, self.clientId)
        self.assertEqual(req.query, self.query)

    def test_execute_insert_query(self):
        req = make_rassrvr_execute_insert_query_req(self.clientId, self.query)
        self.assertEqual(req.client_id, self.clientId)
        self.assertEqual(req.query, self.query)

    def test_get_new_oid(self):
        req = make_rassrvr_get_new_oid_req(self.clientId, self.object_type)
        self.assertEqual(req.client_id, self.clientId)
        self.assertEqual(req.object_type, self.object_type)

    def test_get_object_type(self):
        req = make_rassrvr_get_object_type_req(self.clientId, self.colid)
        self.assertEqual(req.client_id, self.clientId)
        self.assertEqual(req.oid, self.colid)

    def test_get_type_structure(self):
        req = make_rassrvr_get_type_structure_req(self.clientId, self.type_name, self.type_type)
        self.assertEqual(req.client_id, self.clientId)
        self.assertEqual(req.type_name, self.type_name)
        self.assertEqual(req.type_type, self.type_type)

    def test_set_format(self):
        req = make_rassrvr_set_format_req(self.clientId, self.transfer_format, self.format, self.format_params)
        self.assertEqual(req.client_id, self.clientId)
        self.assertEqual(req.transfer_format, self.transfer_format)
        self.assertEqual(req.format, self.format)
        self.assertEqual(req.format_params, self.format_params)

    def test_keep_alive(self):
        req = make_rassrvr_keep_alive_req(self.clientUUID, self.dbsid)
        self.assertEqual(req.client_uuid, self.clientUUID)
        self.assertEqual(req.session_id, self.dbsid)

    def test_begin_streamed_http_query(self):
        req = make_rassrvr_begin_streamed_http_query_req(self.clientUUID, self.data)
        self.assertEqual(req.client_uuid, self.clientUUID)
        self.assertEqual(req.data, self.data)

    def test_get_next_streamed_http_query(self):
        req = make_rassrvr_get_next_streamed_http_query_req(self.clientUUID)
        self.assertEqual(req.uuid, self.clientUUID)


if __name__ == "__main__":
    unittest.main()
