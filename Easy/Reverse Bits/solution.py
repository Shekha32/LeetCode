#Reverse Bits
class Solution:
    
        def reverseBits ( self, n: int ) -> int:
        
                res = 0
                for i in range ( 32 ):
                        res = ( res << 1 ) + ( n & 1 )
                        n >>= 1
                
                return res


def main ():

        ts = Solution ()

        assert ts.reverseBits ( 43261596 ) == 964176192
        assert ts.reverseBits ( 4294967293 ) == 3221225471

main ()
