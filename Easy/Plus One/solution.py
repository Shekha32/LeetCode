#Plus One
class Solution:

	def plusOne ( self, digits: list[int] ) -> list[int]:
                
		st = ''
                
		for num in digits:
			st += str ( num )
			
		return [ int ( i ) for i in str ( int ( st ) + 1 ) ]
    

def main ():

	ts = Solution ()

	assert ts.plusOne ( [ 1, 2, 3 ] ) == [ 1, 2, 4 ]
	assert ts.plusOne ( [ 4, 3, 2, 1 ] ) == [ 4, 3, 2, 2 ]
	assert ts.plusOne ( [ 9 ] ) == [ 1, 0 ]

main ()
