#include <stdio.h>

// Exibir os numeros pares de 1 a MAX_NUMERO

int MAX_NUMERO = 500000;

void loop_v1() {
	for (int i = 0; i <= MAX_NUMERO; i++) {
		if (i % 2 == 0) {
			// printf("%d é par\n", i);
		}
	}
}

void loop_v2() {
	for (int i = 0; i <= MAX_NUMERO; i += 2) {
		// printf("%d é par\n", i);
	}
}

void rec_v1(int n) {
	if (n > MAX_NUMERO) {
		return;
	}

	if (n % 2 == 0) {
		// printf("%d é par!\n", n);
	}

	rec_v1(n + 1);
}

void rec_v2(int n) {
	if (n > MAX_NUMERO) {
		return;
	}

	// printf("%d é par!\n", n);

	rec_v2(n + 2);
}

int main() {
	
    //loop_v1();
	//printf("loop_v1\n");

	// loop_v2();
	// printf("loop_v2\n");

	// rec_v1(0);
	// printf("rec_v1\n");

	rec_v2(0);
	//printf("rec_v2\n");

	return 0;
}