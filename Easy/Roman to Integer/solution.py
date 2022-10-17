#Roman to Integer
class Solution:

	def romanToInt(self, roman: str) -> int:
        
		#print ( 'Roman:', roman, '\n' )
		
		allsymb = { 
			'I': 1,
			'V': 5,
			'X': 10,
			'L': 50,
			'C': 100,
			'D': 500,
			'M': 1000
		}
		
		num = 0         #counter
		prev = ''       #previous symbol
		
		for symb in reversed ( roman ):
		
			if symb not in allsymb.keys():
				exit ( 'Wrong input!' )
                
			else:
				
				if ( symb == 'I' and prev in [ 'V', 'X' ] ) \
				or ( symb == 'X' and prev in [ 'L', 'C' ] ) \
				or ( symb == 'C' and prev in [ 'D', 'M' ] ):
				
					num -= allsymb [ symb ]
				
				else:
					num += allsymb [ symb ]

			#print ( num )
			prev = symb
            
        	#print ( '\nresult = ', num )
        
		return num


def main ():

	ts = Solution ()

	assert ts.romanToInt ( "III" ) == 3
	assert ts.romanToInt ( "LVIII" ) == 58
	assert ts.romanToInt ( "MCMXCIV" ) == 1994

main ()