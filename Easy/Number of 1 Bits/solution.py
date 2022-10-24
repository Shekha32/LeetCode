#Number of 1 Bits
class Solution:
    
        def hammingWeight ( self, n: int ) -> int:

                #I Solution - Str
                #return bin ( n )[2:].count ( '1' )
        
                #II Solution - Bit Manupulation
                count = 0
                
                while n:
                        if n & 1:
                                count += 1
                
                        n >>= 1
                
                return count


def main ():

        ts = Solution ()

        assert ts.hammingWeight ( 11 ) == 3
        assert ts.hammingWeight ( 24 ) == 2

main ()
