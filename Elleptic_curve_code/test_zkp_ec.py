import unittest
from zkp_ec_code import EC_Prover, EC_Verifier, ec_zkp_test
from ecdsa import SigningKey, VerifyingKey, NIST256p

curve = NIST256p
G = curve.generator
order = curve.order

class TestECZKP(unittest.TestCase):
    def test_prover(self):
        x = 5
        prover = EC_Prover(x)
        self.assertEqual(prover.y, x * G)

    def test_verifier(self):
        x = 7
        prover = EC_Prover(x)
        verifier = EC_Verifier(prover.y)
        self.assertIsNotNone(verifier.y)

    def test_ec_zkp(self):
        x = 11
        self.assertTrue(ec_zkp_test(x))

if __name__ == '__main__':
    unittest.main()