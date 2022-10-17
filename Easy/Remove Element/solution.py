#Remove Element
class Solution:
        
        def removeElement ( self, nums: list[int], val: int ) -> int:
        
                k = 0
    
                for num in nums:
                
                        if num != val:
                                nums [ k ] = num
                                k += 1
                
                return k


def main ():

        ts = Solution ()

        assert ts.removeElement ( [ 3, 2, 2, 3 ], 3 ) == 2
        assert ts.removeElement ( [ 0, 1, 2, 2, 3, 0, 4, 2 ], 2 ) == 5

main ()