test_set = ['0', '1', '2', '4', '5', '6' , '7', '8', '9']

k = 6

def solution(prefix, n, idx_c):

    # Se chegou o caso base.
    if n == 0:

        print(prefix)
        return

    """
    for c in test_set:
        solution(prefix + c, n - 1, 0)
    """
    
    # Se falta caractere a ser explorado.
    if idx_c >= len(test_set):
        return
    
    solution(prefix + test_set[idx_c], n - 1, 0)
    solution(prefix, n, idx_c + 1)
    

if __name__=="__main__":

    solution("", k, 0)


