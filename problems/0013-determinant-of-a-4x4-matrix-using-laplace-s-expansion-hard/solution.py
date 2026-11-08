def determinant_4x4(matrix: list[list[int|float]]) -> float:
	# Your recursive implementation here
	n = len(matrix)
	if n == 1: return matrix[0][0]
	res = 0
	matrix_nr = matrix[1:]
	for i in range(n):
		cf = []
		for row in matrix_nr:
			cf.append(row[:i] + row[i+1:])
		cij = determinant_4x4(cf)*matrix[0][i]
		if i%2 == 0:
			res += cij
		else:
			res -= cij

	return res