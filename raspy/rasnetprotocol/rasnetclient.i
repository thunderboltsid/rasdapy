%module rasnetclient
%{
#include "rasnetclientcomm.hh"
using boost::scoped_ptr;
using boost::shared_ptr;
using boost::shared_mutex;
using boost::unique_lock;
using boost::thread;

using common::UUID;
using common::GrpcUtils;

using grpc::Channel;
using grpc::ClientContext;
using grpc::Status;

using rasnet::service::OpenServerDatabaseReq;
using rasnet::service::OpenServerDatabaseRepl;
using rasnet::service::CloseServerDatabaseReq;
using rasnet::service::AbortTransactionRepl;
using rasnet::service::ClientIdentity;
using rasnet::service::AbortTransactionReq;
using rasnet::service::BeginTransactionRepl;
using rasnet::service::BeginTransactionReq;
using rasnet::service::CloseDbReq;
using rasnet::service::CloseDbReq;
using rasnet::service::ConnectReq;
using rasnet::service::ConnectRepl;
using rasnet::service::OpenDbReq;
using rasnet::service::OpenDbRepl;
using rasnet::service::DisconnectReq;
using rasnet::service::Void;
using rasnet::service::CommitTransactionRepl;
using rasnet::service::CommitTransactionReq;
using rasnet::service::DeleteCollectionByNameRepl;
using rasnet::service::DeleteCollectionByNameReq;
using rasnet::service::DeleteCollectionByOidRepl;
using rasnet::service::DeleteCollectionByOidReq;
using rasnet::service::EndInsertMDDRepl;
using rasnet::service::EndInsertMDDReq;
using rasnet::service::EndTransferRepl;
using rasnet::service::EndTransferReq;
using rasnet::service::ExecuteQueryRepl;
using rasnet::service::ExecuteQueryReq;
using rasnet::service::ExecuteUpdateQueryRepl;
using rasnet::service::ExecuteUpdateQueryReq;
using rasnet::service::ExecuteInsertQueryReq;
using rasnet::service::ExecuteInsertQueryRepl;
using rasnet::service::GetCollOidsByNameOrOidRepl;
using rasnet::service::GetCollOidsByNameOrOidReq;
using rasnet::service::GetCollectionByNameOrOidRepl;
using rasnet::service::GetCollectionByNameOrOidReq;
using rasnet::service::GetNewOidRepl;
using rasnet::service::GetNewOidReq;
using rasnet::service::GetNextElementRepl;
using rasnet::service::GetNextElementReq;
using rasnet::service::GetNextMDDRepl;
using rasnet::service::GetNextMDDReq;
using rasnet::service::GetNextTileRepl;
using rasnet::service::GetNextTileReq;
using rasnet::service::GetObjectTypeRepl;
using rasnet::service::GetObjectTypeReq;
using rasnet::service::GetTypeStructureRepl;
using rasnet::service::GetTypeStructureReq;
using rasnet::service::InitUpdateRepl;
using rasnet::service::InitUpdateReq;
using rasnet::service::InsertCollectionRepl;
using rasnet::service::InsertCollectionReq;
using rasnet::service::InsertTileRepl;
using rasnet::service::InsertTileReq;
using rasnet::service::RemoveObjectFromCollectionRepl;
using rasnet::service::RemoveObjectFromCollectionReq;
using rasnet::service::SetFormatRepl;
using rasnet::service::SetFormatReq;
using rasnet::service::StartInsertMDDRepl;
using rasnet::service::StartInsertMDDReq;
using rasnet::service::StartInsertTransMDDRepl;
using rasnet::service::StartInsertTransMDDReq;
using rasnet::service::ClientIdentity;
using rasnet::service::KeepAliveReq;
using rasnet::service::KeepAliveRequest;
using common::ErrorMessage;

using std::string;
%}
RasnetClientComm(std::string rasmgrHost, int rasmgrPort);
RasnetClientCommDestroy();

int connectClient(std::string userName, std::string passwordHash);
int disconnectClient();

int openDB(const char *database);
int closeDB();

int openTA(unsigned short readOnly);
int commitTA();
int abortTA();

void executeQuery(const r_OQL_Query &query, r_Set<r_Ref_Any> &result);
void executeQuery(const r_OQL_Query &query);
void executeQuery(const r_OQL_Query &query, r_Set<r_Ref_Any> &result, int dummy);

