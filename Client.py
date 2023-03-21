import grpc
import protobuf_pb2
import protobuf_pb2_grpc
from zkp_code import Prover

x = 122
prover = Prover(x)

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = protobuf_pb2_grpc.AuthStub(channel)
        register_request = protobuf_pb2.RegisterRequest(user='testuser', y1=prover.y1, y2=prover.y2)
        register_response = stub.Register(register_request)
        print('Registered user')
        r1,r2 = prover.generate_commit()
        # legit authentication
        challenge_request = protobuf_pb2.AuthenticationChallengeRequest(user='testuser', r1=r1, r2=r2)
        challenge_response = stub.CreateAuthenticationChallenge(challenge_request)
        c = challenge_response.c
        print('Got the challenge')
        auth_id = challenge_response.auth_id
        s =  prover.compute_s(c)
        auth_request = protobuf_pb2.AuthenticationAnswerRequest(auth_id= auth_id, s = s)
        response = stub.VerifyAuthentication(auth_request)
        # the authentication is successful if the response is a session ID
        print("Response received: ", response)

if __name__ == '__main__':
    run()