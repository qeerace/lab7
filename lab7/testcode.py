import login
import unittest

class TestCode(unittest.TestCase):
    def test1(self):
        self.assertEqual(login.login('user1','pass1'),1)
    def test2(self):
        self.assertEqual(login.login('user1','pass12'),0)
    def test3(self):
        self.assertEqual(login.login('user12','pass1'),0)
    def test4(self):
        self.assertEqual(login.login('user12','pass2'),0)
if __name__ == '__main__':
    unittest.main()
