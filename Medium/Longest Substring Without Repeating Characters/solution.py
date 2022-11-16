#Longest Substring Without Repeating Characters

class Solution:

        def lengthOfLongestSubstring ( self, s: str ) -> int:

                used = {}
                start = maxlen = 0

                for i in range ( len ( s ) ):

                        if s [ i ] in used and start <= used [ s [ i ] ]:
                                start = used [ s [ i ] ] + 1
                        else:
                                maxlen = max ( maxlen, i - start + 1)

                        used [ s [ i ] ] = i

                return maxlen


def main ():

	ts = Solution ()

	assert ts.lengthOfLongestSubstring ( "abcabcbb" ) == 3
	assert ts.lengthOfLongestSubstring ( "bbbbb" ) == 1
	assert ts.lengthOfLongestSubstring ( "pwwkew" ) == 3

main ()
