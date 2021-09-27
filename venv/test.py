import unittest
from test_module import do_stuff


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        num = 10
        result = do_stuff(num)
        self.assertEqual(result, 15)


unittest.main()