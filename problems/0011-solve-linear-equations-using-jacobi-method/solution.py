import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	D = np.diag(np.diag(A))
	Dinv = np.linalg.inv(D)
	R = A - D
	x = np.zeros_like(b)
	for _ in range(n):
		x = Dinv @ (b - R@x)
	
	return x
