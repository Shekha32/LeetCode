#Search Insert Position
class Solution:

	def searchInsert ( self, nums: list[int], target: int ) -> int:
          
        	#binary search
		l, r = 0, len ( nums ) - 1

		while l <= r:

			mid = ( l + r ) // 2

			if nums [ mid ] == target:
				l = mid
				break
			if target < nums [ mid ]:
				r = mid - 1
			else:
				l = mid + 1
			
		return l


def main ():

	ts = Solution ()

	assert ts.searchInsert ( [ 1, 3, 5, 6 ], 5 ) == 2
	assert ts.searchInsert ( [ 1, 3, 5, 6 ], 2 ) == 1
	assert ts.searchInsert ( [ 1, 3, 5, 6 ], 7 ) == 4

main ()