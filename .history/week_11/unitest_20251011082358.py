
import unittest

def mul(x:int, y:int)->int:
    return x*y





class TestMulFunction(unittest.TestCase):

    def test_mul(self):
        selfassertEqual(mul(1,1),1)
        selfassertEqual(mul(0,3),3)
        selfassertEqual(mul(5,9),45)
        selfassertEqual(mul(-1,9),-9)



if __name__ == "__main__":
    unittest.main()
