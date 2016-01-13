import error_message_pb2 as error
import client_rassrvr_service_pb2 as client
import rasmgr_client_service_pb2 as rasmgr
import time

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class RasMgrClientServiceServicer(rasmgr.BetaRasMgrClientServiceServicer):
    """
    Provides mock methods for testing with a mock server
    """

    def __init__(self):
        pass

    def Connect(self, request, context):
        return rasmgr.ConnectRepl(clientUUID="mockUUID", client_id=0, keepAliveTimeout=100)

    def Disconnect(self, request, context):
        if not request.clientUUID == "mockUUID" and request.clientId == 0:
            raise Exception("Test failed: incorrect client identity during Disconnect request")
        pass

    def OpenDb(self, request, context):
        return rasmgr.OpenDbRepl(dbSessionId="mockDB", serverHostName="mockHost", port=0)

    def CloseDb(self, request, context):
        pass

    def KeepAlive(self, request, context):
        pass


class ClientRassrvrServiceServicer(client.BetaClientRassrvrServiceServicer):
    """
    Provides mock methods for testing a mock server
    """

    def __init__(self):
        pass

    def BeginTransaction(self, request, context):
        pass

    def CommitTransaction(self, request, context):
        pass

    def AbortTransaction(self, request, context):
        pass

    def ExecuteQuery(self, request, context):
        pass

    def ExecuteHttpQuery(self, request, context):
        pass

    def GetNextMDD(self, request, context):
        pass

    def GetNextElement(self, request, context):
        pass

    def GetNextTile(self, request, context):
        pass

    def GetCollectionByNameOrOid(self, request, context):
        pass

def serve():
    server = rasmgr.beta_create_RasMgrClientService_server(RasMgrClientServiceServicer())
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop()

if __name__ == '__main__':
    serve()
