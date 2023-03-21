import random
import hashlib
import json
from Crypto.Util import number
from ecdsa import SigningKey, VerifyingKey, NIST256p

curve = NIST256p
G = curve.generator
order = curve.order

class EC_Prover:
    def __init__(self, x):
        self.x = x
        self.y = x * G

    def generate_k(self):
        self.k = random.randint(1, order-1)
        return self.k * G

    def compute_s(self, c):
        return (self.k - c * self.x) % order

class EC_Verifier:
    def __init__(self, y):
        self.y = y

    def generate_c(self):
        self.c = random.randint(1, order-1)
        return self.c

    def verify(self, r, s):
        return (s * G + self.c * self.y) == r

def ec_zkp_test(x):
    prover = EC_Prover(x)
    verifier = EC_Verifier(prover.y)

    r = prover.generate_k()
    c = verifier.generate_c()
    s = prover.compute_s(c)
    print(r, s)
    return verifier.verify(r, s)
