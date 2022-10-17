#Remove Duplicates from Sorted Array
class Solution:

	def removeDuplicates ( self, nums: list[int] ) -> int:
        
		k = 1

		for n in range ( len ( nums ) - 1 ):
			if nums [ n ] != nums [ n + 1 ]:
				nums [ k ] = nums [ n + 1 ]
				k += 1
			
		return k


def main ():

	ts = Solution ()

	assert ts.removeDuplicates ( [ 1, 1, 2 ] ) == 2
	assert ts.removeDuplicates ( [ 0, 0, 1, 1, 1, 2, 2, 3, 3, 4 ] ) == 5

main ()