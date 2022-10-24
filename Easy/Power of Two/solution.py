#Power of Two
class Solution:
    
        def isPowerOfTwo ( self, n: int ) -> bool:
        
                return n > 0 and n & ( n - 1 ) == 0


def main ():

        ts = Solution ()

        assert ts.isPowerOfTwo ( 0 ) == False
        assert ts.isPowerOfTwo ( 1 ) == True
        assert ts.isPowerOfTwo ( -32 ) == False
        assert ts.isPowerOfTwo ( 16 ) == True

main ()
