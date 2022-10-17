#Valid Parentheses
class Solution:

	def isValid ( self, s: str ) -> bool:
	
		table = {
			"(": ")",
			"[": "]",
			"{": "}"
		}
		
		res = True
		expected = []
		
		if len ( s ) % 2 != 0:
			res = False
	
		else:
	
			for symb in s:

				if symb in table.keys():
					expected.append ( table [ symb ] )

				elif symb in table.values():
		    
					if expected == [] or symb != expected.pop():
						res = False
						break

				else:
					res = False
					break

		return res if expected == [] else False
    

def main ():

	ts = Solution ()

	assert ts.isValid ( "()" ) == True
	assert ts.isValid ( "()[]{}" ) == True
	assert ts.isValid ( "(]" ) == False
	assert ts.isValid ( "()[{()}]" ) == True
	assert ts.isValid ( "()[{(}]" ) == False

main ()
