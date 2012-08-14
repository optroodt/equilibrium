#/usr/bin/python

def equi ( A ):
	
	length = len(A)
	left = 0
	right = sum(A)
	eqs = []

	for index, item in enumerate(A):
		if index+1 >= length:
			continue

		left = left + A[index]
		right = right - A[index]
		
		if left == right - A[index+1]:
			eqs.append(index+1)

	return eqs

print equi([])
print equi([-7,1,5,2,-4,3,0]);
eq = [ 1 for i in range(1,1000) ]
print equi(eq)
eq = [ -1 for i in range(1,10000) ]
print equi(eq)
