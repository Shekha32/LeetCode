#Longest Common Prefix
class Solution:
    
	def longestCommonPrefix ( self, strs: list[str] ) -> str:
        
        	#print ( 'strs: ', strs )
        
		flag = False
		res = shortword = min ( strs, key=len )       #shortest word in strs
		
		for i, symb in enumerate ( shortword ):
		
			#print ( i, symb )
		
			for other in strs:
			
				#print ('\t', other)
			
				if other [ i ] != symb:
					flag = True
					res = shortword [:i]
					break
		
			if flag:
				break
			
		return res
                    
        
def main ():

	ts = Solution ()

	assert ts.longestCommonPrefix ( [ "flower", "flow", "flight" ] ) == "fl"
	assert ts.longestCommonPrefix ( ["dog","racecar","car"] ) == ""

main ()
