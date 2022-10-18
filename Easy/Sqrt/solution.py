#Sqrt(x)
class Solution:
    
	def mySqrt ( self, x: int ) -> int:
        
		#I Solution
		#return int ( sqrt ( x ) )
	
		#II Solution
		#i = 0
		
		#while ( ( i + 1 ) * ( i + 1 ) <= x ):
			#i += 1
		
		#return i

		#III Solution - Binary Search
		res = 0
		left, rigth = 0, x
		
		while left <= rigth:
		
			mid = ( rigth + left ) // 2
            
			#print ( "\nleft", left )
			#print ( "rigth", rigth )
			#print ( "mid", mid )
			
			if ( ( mid * mid <= x ) and ( ( mid + 1 ) * ( mid + 1 ) > x ) ):
				res = mid
				break
            
			if mid * mid <= x:
				left = mid + 1
			
			elif ( mid + 1 ) * ( mid + 1 ) > x:
				rigth = mid - 1
		
		return res


def main ():

        ts = Solution ()

        assert ts.mySqrt ( 0 ) == 0
        assert ts.mySqrt ( 1 ) == 1
        assert ts.mySqrt ( 3 ) == 1
        assert ts.mySqrt ( 4 ) == 2
        assert ts.mySqrt ( 8 ) == 2
        assert ts.mySqrt ( 9 ) == 3
        assert ts.mySqrt ( 16 ) == 4
        assert ts.mySqrt ( 24 ) == 4
        assert ts.mySqrt ( 25 ) == 5

main()
