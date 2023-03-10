import unittest

from primes import is_prime


class PrimesTests(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(7))

        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(-1))


# 現在はテスト探索によりtestで始まる関数を実行する
class OtherTests(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    # 実行されない
    def is_not_test_prefix(self):
        self.assertFalse(True)


if __name__ == "__main__":
    unittest.main()
