#Write an algorithm such that if an element in an MxN matrix 
#is 0, its entire row and column is set to 0.


def setRowAndColumnToZero(rectangle_matrix):
#don't want to detect 0 multiple times and re-do the operation 
#unessisarily. Find all 0's first, then replace as needed.
#need to loop through matrix twice....seems like a poor design
#redo it later
	row_num = 0
	column_num = 0
	zero_rows=set()
	zero_columns=set()
	for row in rectangle_matrix:
		#realized that you can erase the whole row before the second
		#scan as long as you store those columns, but you still need
		#to scan again for the columns, so probably not worth the extra
		#complexity / confusion for next person reading it
		for column in row:
			if rectangle_matrix[row_num][column_num] == 0:
				zero_rows.add(row_num)
				zero_columns.add(column_num)
			column_num += 1
		row_num += 1
		column_num = 0
	#reset indicies
	row_num = 0
	column_num = 0
	#use the fact that empty sequences are false & 
	#check there is a zero before traversing
	if zero_rows:
		for row in rectangle_matrix:
			if row_num in zero_rows:
				rectangle_matrix[row_num] = [0]*len(row)
			else:
				for column in row:
					if column_num in zero_columns:
						print 
						rectangle_matrix[row_num][column_num] = 0
					column_num += 1
			row_num += 1
			column_num = 0
	return rectangle_matrix

print "Test1: 0 1 2"
print "Test1: 3 4 5"
print "Test1: 6 7 8"
print setRowAndColumnToZero([[0,1,2],[3,4,5],[6,7,8]]) == [[0,0,0],[0,4,5],[0,7,8]]