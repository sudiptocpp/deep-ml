def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	trace = matrix[0][0] + matrix[1][1]
	det = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
	fst = trace/2
	D = (trace*trace - 4*det)
	if D < 0: return []
	snd = (trace*trace - 4*det)**0.5 / 2

	return [fst + snd, fst - snd]