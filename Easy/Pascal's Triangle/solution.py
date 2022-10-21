#Pascal's Triangle
class Solution:
    
        def generate ( self, numRows: int ) -> list [ list [ int ] ]:
        
                res = [ [ 1 ] ]
                
                for i in range ( 1, numRows ):

#                       explanation: Any row can be constructed using the offset sum of the previous row. Example:
#                          1 3 3 1 0 
#                       +  0 1 3 3 1
#                       =  1 4 6 4 1

                        res += [ list ( map ( lambda x, y: x + y, res [ -1 ] + [ 0 ], [ 0 ] + res [ -1 ] ) ) ]
                
                return res


def main ():

        ts = Solution ()

        assert ts.generate ( 1 ) == [ [ 1 ] ]
        assert ts.generate ( 3 ) == [ [ 1 ], [ 1, 1 ], [ 1, 2, 1 ] ]
        assert ts.generate ( 5 ) == [ [ 1 ], [ 1, 1 ], [ 1, 2, 1 ], [ 1, 3, 3, 1 ], [ 1, 4, 6, 4, 1 ] ]

main ()
