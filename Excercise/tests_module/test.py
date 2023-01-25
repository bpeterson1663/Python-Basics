import unittest
import do_stuff

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = do_stuff.add_three(test_param)
        self.assertEqual(result, 13)
    def test_do_wrong_stuff(self):
        test_param = "not a number"
        result = do_stuff.add_three(test_param)
        self.assertTrue(isinstance(result, ValueError))
        
unittest.main()