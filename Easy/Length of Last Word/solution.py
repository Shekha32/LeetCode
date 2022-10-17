#Length of Last Word
class Solution:

	def lengthOfLastWord ( self, s: str ) -> int:
        
		length = 0
		s = s.rstrip ( ' ' )    #delete ' ' from the right side
			
		for symb in s [::-1]:
			if symb != ' ':
				length += 1
			else:
				break
		
		return length        


def main ():

	ts = Solution ()

	assert ts.lengthOfLastWord ( "Hello World" ) == 5
	assert ts.lengthOfLastWord ( "   fly me   to   the moon  " ) == 4
	assert ts.lengthOfLastWord ( "luffy is still joyboy" ) == 6
	assert ts.lengthOfLastWord ( " I love  Pink   Floyd  " ) == 5


main ()