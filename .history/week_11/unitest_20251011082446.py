
import unittest

def mul(x:int, y:int)->int:
    return x*y





class TestMulFunction(unittest.TestCase):

    def test_mul(self):
        self.assertEqual(mul(1,1),1)
        self.assertEqual(mul(0,3),3)
        self.assertEqual(mul(5,9),45)
        self.assertEqual(mul(-1,9),-9)



if __name__ == "__main__":
    unittest.main()
