#Two Sum
class Solution:

	def twoSum ( self, nums: list[int], target: int ) -> list[int]:
        
		#print ( 'nums: ', nums, ', target = ', target )
        
		res = []
		check = {}
        
		for n in range ( len ( nums ) ):
		
			if nums [ n ] in check.keys ():
				res = [ check [ nums [ n ] ] , n ]
			
			else:
				check [ target - nums [ n ] ] = n
		
		#print ( check )
		#print ( res )
		
		return res


def main ():

	ts = Solution ()

	assert ts.twoSum ( [ 2, 7, 11, 15 ], 9 ) == [ 0, 1 ]
	assert ts.twoSum ( [ 3, 2, 4 ], 6 ) == [ 1, 2 ]
	assert ts.twoSum ( [ 3, 3 ], 6 ) == [ 0, 1 ]

main ()
