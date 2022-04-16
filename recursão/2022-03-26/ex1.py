# https://www.geeksforgeeks.org/print-all-combinations-of-given-length/

test_set = ('0','1','2','4','5','6','7','8','9')
test_k = 4

def convert_to_base(i, base, k, characters):
	"""
	(4, 2) -> [1, 0, 0]
	(6, 2) -> [1, 1, 0]
	"""
	converted = []

	ci = i
	while ci > 0:
		idiv = ci // base
		rest = ci % base

		char = characters[rest]
		converted.append(char)

		ci = idiv

	# completa com 0s para ter k digitos
	while len(converted) < k:
		converted.append(characters[0])

	# inverte
	converted.reverse()

	return ''.join(converted)


def combinations(characters, k):
	base = len(characters)
	total = base ** k

	for i in range(total):
		converted = convert_to_base(i, base, k, characters)
		print(converted)


combinations(test_set, test_k)
