#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char test_set[] = {'0', '1', '2', '4', '5', '6' , '7', '8', '9'};
int k = 6, set_size = sizeof(test_set);

void solution(char *prefix, int n, int idx_c){

    // Se for o nosso caso base.
    if (n == 0){
        printf("%s\n", prefix);
        return;
    }

    if (idx_c >= set_size){
        return;
    }
    char *new_prefix = malloc(strlen(prefix) + 2);
    sprintf(new_prefix, "%s%c", prefix, test_set[idx_c]);
    solution(new_prefix, n - 1, 0);
    free(new_prefix);
    solution(prefix, n, idx_c + 1);
}

int main(void){

    solution("", k, 0);
    return 0;
}

/*
real    0m16,977s
user    0m0,675s
sys     0m1,629s
*/