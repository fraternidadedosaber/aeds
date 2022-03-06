# Exibir os números pares de 1 a 100

MAX_NUMERO = 950

def loop_v1():
	for i in range(MAX_NUMERO):
		if i % 2 == 0:
			print(i, "é par!")

def loop_v2():
	for i in range(0, MAX_NUMERO, 2):
		print(i, "é par!")

def rec_v1(n):
	if n > MAX_NUMERO:
		return
	
	if n % 2 == 0:
		print(n, "é par!")

	rec_v1(n + 1)

def rec_v2(n):
	if n > MAX_NUMERO:
		return

	print(n, "é par!")
	rec_v2(n + 2)


if __name__ == "__main__":
	# print("loop_v1")
	# loop_v1()
	
	
	"""
	print("loop_v2")
	loop_v2()
	"""

	rec_v1(0)
	print("rec_v1")
	
	"""
	rec_v2(0)
	print("rec_v2")
	"""
# loop_v1 = 31s
# loop_v1 = 36s
# rec_v1 = 