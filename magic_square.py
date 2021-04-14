def magic_square(n:int):
	"""Get a n×n magic square in list

	The function now only handles the magic squere 
	those n is n/2 != 0 and return a result in list, 
	otherwise it returns None.

	For example:
	magic_square(3) will return [[8, 1, 6], [3, 5, 7], [4, 9, 2]].
	magic_square(4) will return None since 4/2 == 0.
	"""

	if n%2 != 0:
		res = [[0 for i in range(0,n)] for i in range(0,n)]
		line, column = 0, n//2
		res[line][column] = 1

		for num in range(2, n**2 + 1):
			line_cp, column_cp = line, column

			if line - 1 == - 1:
				line = n - 1
			else:
				line = line - 1

			if column + 1 == n:
				column = 0
			else:
				column = column + 1

			if res[line][column] == 0:
				res[line][column] = num
			else:
				line, column = line_cp, column_cp
				line = line + 1
				res[line][column] = num
				
		return res

import sys

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("""\
Command syntax: magic_square.py n

For example: 
Typing command 'magic_square.py 3' will print a 3×3 magic square.

The script now only handles the magic squere those n is n/2 != 0,
otherwise it will print 'None'.""");
	else:
		print(*magic_square(int(sys.argv[1])), sep = "\n")

