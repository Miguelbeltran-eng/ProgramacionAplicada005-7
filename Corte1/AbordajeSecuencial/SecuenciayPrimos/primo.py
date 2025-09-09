import time
import math

def es_primo(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    limite = int(math.sqrt(num))
    for i in range(3, limite + 1, 2):
        if num % i == 0:
            return False
    return True

try:
    num = 1
    while True:
        if es_primo(num):
            print(f"{num} es primo")
        else:
            print(f"{num} no es primo")
        num += 1
        time.sleep(1)
except KeyboardInterrupt:
    print("\nPrograma terminado por el usuario.")
