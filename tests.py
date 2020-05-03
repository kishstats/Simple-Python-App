import unittest

from myapp import run_myapp


class DummyTest(unittest.TestCase):
    def test_run_myapp(self):
        print("run_myapp_test")
        result = run_myapp()
        self.assertEqual(result, 'It works')


if __name__ == "__main__":
    unittest.main()