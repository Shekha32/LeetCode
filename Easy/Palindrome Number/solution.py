#Palindrome Number
class Solution:

	def isPalindrome ( self, x: int ) -> bool:
        
		#print ( str ( x ) )
		#print ( str ( x ) [::-1] )
        
        	return True if str ( x ) == str ( x ) [::-1] else False
        

def main ():

	ts = Solution ()

	assert ts.isPalindrome ( 121 ) == True
	assert ts.isPalindrome ( -121 ) == False
	assert ts.isPalindrome ( 10 ) == False

main ()
