#Can Place Flowers
class Solution:
    
        def canPlaceFlowers ( self, flowerbed: list[int], n: int ) -> bool:
        
                return sum ( ( len ( zeros ) - 1 ) // 2 for zeros in ''.join ( map ( str, [ 0 ] + flowerbed + [ 0 ] ) ).split ( '1' ) ) >= n


def main ():

        ts = Solution ()

        assert ts.canPlaceFlowers ( [1,0,0,1], 1 ) == False
        assert ts.canPlaceFlowers ( [1,0,0,0,1], 1 ) == True
        assert ts.canPlaceFlowers ( [1,0,0,0,1], 2 ) == False
        assert ts.canPlaceFlowers ( [1,0,1,0,1,0,1], 1 ) == False
        assert ts.canPlaceFlowers ( [0,1,0,0,1,0,0], 1 ) == True

main ()
