
#Median of Two Sorted Arrays

class Solution:

        def __kth ( self, a: int, b: int, k: int ) -> float:

                if not a:
                        return b [ k ]
                if not b:
                        return a [ k ]

                ia, ib = len ( a ) // 2, len ( b ) // 2
                ma, mb = a [ ia ], b [ ib ]
                
                #when k is bigger than the sum of a and b's median indices 
                if ia + ib < k:
                        #if a's median is bigger than b's, b's first half doesn't include k
                        if ma > mb:
                                return self.__kth ( a, b[ib + 1:], k - ib - 1 )
                        else:
                                return self.__kth ( a[ia + 1:], b, k - ia - 1 )
                
                #when k is smaller than the sum of a and b's indices
                else:
                        #if a's median is bigger than b's, a's second half doesn't include k
                        if ma > mb:
                                return self.__kth ( a[:ia], b, k )
                        else:
                                return self.__kth ( a, b[:ib], k )


        def findMedianSortedArrays ( self, A: list, B: list ) -> float:

                l = len ( A ) + len ( B )

                if l % 2 == 1:
                        return self.__kth ( A, B, l // 2 )
                else:
                        return ( self.__kth ( A, B, l // 2 ) + self.__kth ( A, B, l // 2 - 1 ) ) / 2.   


def __main():

        ts = Solution()
        assert ts.findMedianSortedArrays ( [ 0 ], [ 0 ] ) == 0.0
        assert ts.findMedianSortedArrays ( [ 0 ], [ 0, 1 ] ) == 0.0
        assert ts.findMedianSortedArrays ( [ 1, 2 ], [ 2, 3 ] ) == 2.0
        assert ts.findMedianSortedArrays ( [ 0, 1, 2 ], [ 3, 4, 5, 6 ] ) == 3.0


if __name__ == '__main__':
        __main ()
