
import pytest


class Test_credence:
    x=10
    y=5
    # @pytest.mark.skipif(x<y, reason='There is a bug in the test case')
    def test_sum_001(self):
        a=3
        b=7
        sum=a+b
        print('sum of a and b is:'+ str(sum))
        if sum==10:
            assert True
        else:
            assert False
