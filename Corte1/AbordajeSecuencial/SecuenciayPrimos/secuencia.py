import time

try:
    num = 1
    while True:
        if num % 2 == 0:
            print(f"{num} es par")
        else:
            print(f"{num} es impar")
        num += 1
        time.sleep(0.5)  # Espera 1 segundo para que no sea muy rápido
except KeyboardInterrupt:
    print("\nPrograma terminado por el usuario.")
