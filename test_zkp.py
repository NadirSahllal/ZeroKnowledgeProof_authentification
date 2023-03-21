import unittest
from zkp_code import Prover, Verifier, zkp_test

class TestZKP(unittest.TestCase):
    def test_prover(self):
        x = 15
        q = 23
        prover = Prover(x)
        self.assertEqual(prover.y1, pow(4, x, q))
        self.assertEqual(prover.y2, pow(9, x, q))

    def test_verifier(self):
        x = 7
        q = 23
        prover = Prover(x)
        verifier = Verifier(prover.y1, prover.y2)
        self.assertIsNotNone(verifier.y1)
        self.assertIsNotNone(verifier.y2)

    def test_zkp(self):
        x = 11
        self.assertTrue(zkp_test(x))

if __name__ == '__main__':
    unittest.main()