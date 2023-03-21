import random
import hashlib
import json
from Crypto.Util import number

# Constants
g = 4
h = 9
q = 23 #number.getPrime(256)
order = 11

class Prover:
    def __init__(self, x):
        self.x = x
        self.y1 = pow(g, x, q)
        self.y2 = pow(h, x, q)
        self.k = random.randint(1, q-1)

    def generate_commit(self):
        return (pow(g, self.k, q), pow(h, self.k, q))

    def compute_s(self, c):
        return (self.k - c * self.x) % order

class Verifier:
    def __init__(self, y1, y2):
        self.y1 = y1
        self.y2 = y2

    def generate_c(self):
        self.c = random.randint(1, q-1)
        return self.c

    def verify(self, r1, r2, s):
        return (pow(g, s, q) * pow(self.y1, self.c, q)) % q == r1 and (pow(h, s, q) * pow(self.y2, self.c, q)) % q == r2

def zkp_test(x):
    prover = Prover(x)
    verifier = Verifier(prover.y1, prover.y2)

    r1, r2 = prover.generate_commit()
    c = verifier.generate_c()
    s = prover.compute_s(c)
    return verifier.verify(r1, r2, s)


# Function 1: Prover registers password with verifier and returns client ID
def register_new_client(login, password, g, h):
    # Generate random salt
    salt = secrets.token_bytes(16)
    stretch_count=1000
    # Stretch password using PBKDF2-HMAC-SHA256
    password_bytes = str(password).encode('utf-8')
    stretched_password = hashlib.pbkdf2_hmac('sha256', password_bytes, salt, stretch_count)
    
    # Convert stretched password to integer x
    x = int.from_bytes(stretched_password, byteorder='big')
    
    # Generate random value r
    r = secrets.randbelow(g-1) + 1
    
    # Calculate y1 and y2
    y1 = pow(g, r)
    y2 = (pow(h, r) * x) % g
    
    # Generate client ID based on login
    login_bytes = str(login).encode('utf-8')
    hashed_login = hashlib.sha256(login_bytes).digest()
    client_id = hashed_login.hex()
    
    # Return y1, y2, salt, stretch_count, and client ID
    return y1, y2, client_id

# Function 2: Verifier receives y1, y2 and saves it in cache with client ID, salt, and stretch count
def save_client(y1, y2, client_id):
    # Load existing cache from file, if it exists
    filename = 'clients.json'
    try:
        with open(filename, 'r') as f:
            cache = json.load(f)
    except FileNotFoundError:
        cache = {}
    
    # Save y1, y2, salt, and stretch count in cache with client ID as key
    cache[client_id] = {'y1': y1, 'y2': y2}
    
    # Save updated cache to file
    with open(filename, 'w') as f:
        json.dump(cache, f)