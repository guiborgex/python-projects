import os
import time
from multiprocessing import Process

def child_process():
    print(f"Processo filho: PID={os.getpid()}, PPID={os.getppid()}")
    time.sleep(2)
    print("Processo filho encerrando.")

def main():
    print(f"Processo pai: PID={os.getpid()}")

    processo = Process(target=child_process)
    processo.start()

    print(f"Processo pai criou o filho com PID={processo.pid}")

    processo.join()

    print("Processo pai: Filho terminou.")

if __name__ == "__main__":
    main()