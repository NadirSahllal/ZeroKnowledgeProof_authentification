# ZeroKnowledgeProof_authentification

Authentication Setup Using gRPC and Protobuf

## Description
This project focuses on creating an authentication setup following client and server using gRPC described in protobuf.proto. We have implemented two authentication codes: one using exponentiation and the other using elliptic curves. The code is written in English, and we mainly use the exponentiation for the test case, but we could use the elliptic curve code with some slight modifications. The authentication code has unit tests in place.

## Usage
Start by installing the necessary dependances

```
pip install -r requirements.txt
```
to run the set up using Docker:
 ```
   docker build -t grpc-client -f Dockerfile.client . 
   docker build -t grpc-server -f Dockerfile.server .
```
Then run:
```
  docker-compose up   
```
while to run the server and client locally a change is needed in line 13 of the client.py file:
replace:
```
 grpc.insecure_channel('grpc-server:8000') as channel: 
```
with:
```
 with grpc.insecure_channel('localhost:8000') as channel: 
```

 making the previous change, run :
```
  python Server.py
```
In a different terminal run:
```
  python Client.py
```
This will start the server and client applications. The server will listen on localhost:50051, and the client will connect to it. The client will then authenticate the user using the authentication code implemented in the project.

## Improvements

**code Modalization**: The spliting of the code into different modules could probably be improved.

**Error handling**: Add proper error handling to cover scenarios where inputs might be invalid or when the cache file is not accessible.

**Unused Functionality**: The register_new_client function is not currently used, but it is an example of how we could secure user credentials. We could implement this function to allow clients to register their credentials and store them securely.

**Secure Random Generation**: To prevent side-channel attacks, we could use a more secure random number generator for generating cryptographic keys.

**Extended Authentication Flow**: We could extend the flow of authentication to include additional security measures.

**Additional Tests**: We could add additional tests to the base code to ensure that it is secure against different types of attacks.

**Use a more secure prime and think about storage options for the public information**


Overall, this project was a great opportunity for me to work with gRPC and Protobuf, which were both completely new to me. This project was not only interesting but also helped me brush up on concepts I haven't worked with in a while.
