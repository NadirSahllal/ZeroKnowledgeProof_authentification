import grpc
from concurrent import futures
import protobuf_pb2
import protobuf_pb2_grpc
import json
import uuid
from zkp_code import save_client, Verifier

class AuthService(protobuf_pb2_grpc.AuthServicer):
    def __init__(self):
        # Initialize the session dictionary
        self.sessions = {}
        self.verifier = None
    
    def Register(self, request, context):
        save_client(request.y1, request.y2, request.user)
        response = protobuf_pb2.RegisterResponse()
        return response
    
    def CreateAuthenticationChallenge(self, request, context):
        session_id = str(uuid.uuid4())
        with open('clients.json') as json_file:
            data = json.load(json_file)
        clientData = data[request.user]
        self.verifier = Verifier(clientData['y1'], clientData['y2'])
        c = self.verifier.generate_c()
        self.sessions[session_id] = {'user': request.user, 'r1': request.r1,
                             'r2': request.r2, 'y1': clientData['y1'], 'y2': clientData['y2'], 'c': c}
        
        response = protobuf_pb2.AuthenticationChallengeResponse(auth_id=session_id, c=c)
        return response

    def VerifyAuthentication(self, request, context):
        print('we here')
        session_id =  request.auth_id
        session = self.sessions[session_id]
        s = request.s

        print('did we get here')
        if self.verifier.verify(session['r1'], session['r2'], s):
            print('did we get here')
            return protobuf_pb2.AuthenticationAnswerResponse(session_id=session_id)
        else:
            context.set_details('Authentication failed')
            context.set_code(grpc.StatusCode.UNAUTHENTICATED)
            return protobuf_pb2.AuthenticationAnswerResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    protobuf_pb2_grpc.add_AuthServicer_to_server(AuthService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()