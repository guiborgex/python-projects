import threading
import time

def task(name, duration):
    print(f"Thread {name}: Iniciando tarefa por {duration} segundos.")
    time.sleep(duration)
    print(f"Thread {name}: Tarefa concluída.")

def main():
    print("Programa principal: Iniciando threads.")

    thread1 = threading.Thread(target=task, args=("A", 3))
    thread2 = threading.Thread(target=task, args=("B", 2))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Programa principal: Todas as threads concluídas.")

if __name__ == "__main__":
    main()