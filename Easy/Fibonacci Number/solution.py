#Fibonacci Number
class Solution:
    
        def fib ( self, n: int ) -> int:
        
#               #I Solution - Memoized Recursive
#               mem = { 0: 0, 1: 1 }
        
#               def calc ( n ):
            
#                       if n in mem:
#                               return mem [ n ]
            
#                       mem [ n ] = calc ( n - 1 ) + calc ( n - 2 )
#                       return mem [ n ]
        
#               return calc ( n )


                #II Solution - Dynamic Programming
                fb = [ 0, 1 ]
        
                for i in range ( 2, n + 1 ):
                        fb.append ( fb [ i - 1 ] + fb [ i - 2 ] )
                
                return fb [ n ]


def main ():

        ts = Solution ()

        assert ts.fib ( 1 ) == 1
        assert ts.fib ( 3 ) == 2
        assert ts.fib ( 6 ) == 8

main ()