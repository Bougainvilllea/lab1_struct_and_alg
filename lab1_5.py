""" Проведите эксперимент, сравнивающий производительность оператора in для множеств и
    списков. Покажите их поведение при помощи графика зависимости времени от количества
    входных данных. """


import time
import numpy as np
import matplotlib.pyplot as plt



def foo_1(list):
    if 0 in list:
        return True
    else: return False

def foo_2(list):
    set_from_list = set(list)
    if 0 in set_from_list:
        return True
    else:
        return False


def measure_algorithm_time(foo, n):
    num = np.random.randint(0, 100, n)
    tic = time.time()
    foo(num)
    toc = time.time()

    return toc - tic


def create_performance_chart():
    input_sizes = list(range(500, 2100, 50))
    times_1 = []
    times_2 = []

    print("Измеряем время выполнения для разных размеров")

    for size in input_sizes:
        execution_time_1 = measure_algorithm_time(foo_1, size)
        execution_time_2 = measure_algorithm_time(foo_2, size)

        times_1.append(execution_time_1)
        times_2.append(execution_time_2)

        print(f"Размер: {size}, Время foo_1: {execution_time_1:.6f}s, foo_2: {execution_time_2:.6f}s")

    plt.figure(figsize=(12, 8))
    plt.plot(input_sizes, times_1, marker='o', linewidth=2, markersize=8, color='red')
    plt.plot(input_sizes, times_2, marker='s', linewidth=2, markersize=8, color='green')

    plt.title('Зависимость времени выполнения алгоритма от размера входных данных',
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Размер входных данных (количество элементов)', fontsize=14)
    plt.ylabel('Время выполнения (секунды)', fontsize=14)

    plt.grid(True, alpha=0.3)

    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    create_performance_chart()

