import error_message_pb2 as error
import client_rassrvr_service_pb2 as client
import rasmgr_client_service_pb2 as rasmgr
import time

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class RasMgrClientServiceServicer(rasmgr.BetaRasMgrClientServiceServicer):
    """
    Provides mock methods for testing with a mock server
    """

    def Connect(self, request, context):
        print("Invoking Connect")
        repl = rasmgr.ConnectRepl(clientUUID="mockUUID", clientId=0, keepAliveTimeout=100)
        return repl

    def Disconnect(self, request, context):
        print("Invoking Disconnect")
        if not request.clientUUID == "mockUUID" and request.clientId == 0:
            raise Exception("Test failed: incorrect client identity during Disconnect request")
        pass

    def OpenDb(self, request, context):
        print("Invoking OpenDb")
        return rasmgr.OpenDbRepl(dbSessionId="mockDB", serverHostName="mockHost", port=0)

    def CloseDb(self, request, context):
        print("Invoking CloseDb")

    def KeepAlive(self, request, context):
        print("Invoking KeepAlive")


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
        try:
            server.stop()
        except:
            print("Oops!")

if __name__ == '__main__':
    serve()
