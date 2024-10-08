import random

def find_duos(n):
    duos = []
    for i in range(1, n + 1):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                duos.append((i, j))
    return duos

def genpassword(n):
    duos = find_duos(n)
    result = ''.join(f'{i}{j}' for i, j in duos)
    return result

n1 = random.choice(range(3,21))
result = genpassword(n1)
print(f'Пароль для числа {n1} = {result}')