#Add Binary
class Solution:

	def addBinary ( self, a: str, b: str ) -> str:

		return bin ( int ( a, 2 ) + int ( b, 2 ) ) [2:]


def main ():

	ts = Solution ()

	assert ts.addBinary ( "11", "1" ) == "100"
	assert ts.addBinary ( "1010", "1011" ) == "10101"

main ()
