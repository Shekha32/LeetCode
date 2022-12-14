#Power of Two
class Solution:
    
        def isPowerOfTwo ( self, n: int ) -> bool:
                
                # if n is the power of two:
                # n = 2 ^ 0 = 1 = 0b0000...00000001, and (n - 1) = 0 = 0b0000...0000.
                # n = 2 ^ 1 = 2 = 0b0000...00000010, and (n - 1) = 1 = 0b0000...0001.
                # n = 2 ^ 2 = 4 = 0b0000...00000100, and (n - 1) = 3 = 0b0000...0011.
                # n = 2 ^ 3 = 8 = 0b0000...00001000, and (n - 1) = 7 = 0b0000...0111.
                # we have n & (n-1) == 0b0000...0000 == 0
                # Otherwise, n & (n-1) != 0.
                # For example, n =14 = 0b0000...1110, and (n - 1) = 13 = 0b0000...1101.
                # Time complexity = O(1)
                
                return n > 0 and n & ( n - 1 ) == 0


def main ():

        ts = Solution ()

        assert ts.isPowerOfTwo ( 0 ) == False
        assert ts.isPowerOfTwo ( 1 ) == True
        assert ts.isPowerOfTwo ( -32 ) == False
        assert ts.isPowerOfTwo ( 16 ) == True

main ()
