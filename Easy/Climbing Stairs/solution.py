#Climbing Stairs
class Solution:
    
        def climbStairs ( self, n: int ) -> int:
        
                #I Solution - Recursion
                #base = { 1: 1, 2: 2 }
                
                #def climb ( n ):
                
                #if n in base:
                        #return base [ n ]
                #else:
                        #base [ n ] = climb ( n - 1 ) + climb ( n - 2 )         #fill in the dict for already computed operations
                        #return base [ n ]  
                
                #return climb ( n )


                #II Solution - Dynamic Programming
                if n == 1: return 1
                if n == 2: return 2
                
                mas = [ 0 ] * ( n + 1 )
                mas [ 1 ] = 1
                mas [ 2 ] = 2
                
                for i in range ( 3, n + 1 ):
                        mas [ i ] = mas [ i - 1 ] + mas [ i - 2 ]       #Fibonacci series
                
                return mas [ n ]


def main ():

        ts = Solution ()

        assert ts.climbStairs ( 2 ) == 2
        assert ts.climbStairs ( 5 ) == 8
        assert ts.climbStairs ( 10 ) == 89
        assert ts.climbStairs ( 43 ) == 701408733

main ()
