import unittest


class Calculator:
    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            raise ValueError("Divide by Zero")
        return a / b

# if __name__ == "__main__":
# 	calc = Calculator()
# 	print(calc.sum(1, 2))


class TestCalculator(unittest.TestCase):

    # Before each test
    def setUp(self):
        self.calc = Calculator()

    # Test sum
    # def test_sum(self):
    # 	res = self.calc.sum(1, 5)
    # 	self.assertEqual(res, 7)

    # def test_sub(self):
    # 	res = self.calc.sub(7, 5)
    # 	self.assertEqual(res, 2)

    # def test_mul(self):
    # 	res = self.calc.mul(2, 5)
    # 	self.assertEqual(res, 10)

    # def test_div(self):
    # 	res = self.calc.div(9, 3)
    # 	self.assertEqual(res, 3)

    # def test_div_by_zero(self):
    # 	with self.assertRaises(ValueError):
    # 		self.calc.div(5, 0)

    def tearDown(self):
        # Another clean-up code
        pass

    def test_add(self):
        res = self.calc.sum(5, 3)
        self.assertEqual(res, 8, "Wrong result: sum")

    def test_subtract(self):
        res = self.calc.sub(10, 4)
        self.assertEqual(res, 6, "Wrong result: subtract")

    def test_multiply(self):
        res = self.calc.mul(2, 3)
        self.assertEqual(res, 6, "Wrong result: multiply")

    def test_divide(self):
        res = self.calc.div(8, 4)
        self.assertEqual(res, 2, "Wrong result: divide")

    def test_div_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.div(5, 0)

    @unittest.skip("Skip this test")
    def test_skip_example(self):
        self.fail("This test will not run")

    @unittest.skipIf(True, "Skip this test with IF")
    def test_skip_if_example(self):
        self.fail("This test will not run with IF")

    @unittest.expectedFailure
    def test_expected_failure(self):
        res = self.calc.sum(2, 2)
        self.assertEqual(res, 5, "This test granted FAIL")
