""" 1 вариант """

""" 1) Что выполняет приведенная функция? """

# принимает число =>
# проверяет не равно ли оно нулю,  если нет =>
# берет элемент digits под номером остатка i на деленого 10 =>
# добавляет этот элемент в начало строки result до тех пор пока =>
# целочисленное деление на 10 не даст 0

"""  2) Какова вычислительная сложность алгоритма (в О-нотации)? """

# имеет логарифмическую сложность O(log n)
# rоличество итераций цикла равно количеству цифр в числе i
# на каждой итерации уменьшает объём данных для обработки, что характерно лог. сложности


import time
import numpy as np
import matplotlib.pyplot as plt


def foo(i):  # i - число
    digits = "0123456789"
    if i == 0:
        return "0"
    result = ""
    while i > 0:
        result = digits[i % 10] + result
        i = i // 10
    return result


def measure_algorithm_time(n):
    num = np.random.randint(0, 10000)
    tic = time.time()
    foo(num)
    toc = time.time()

    return toc - tic


def create_performance_chart():
    input_sizes = list(range(500, 2100, 50))
    times = []

    print("Измеряем время выполнения для разных размеров")

    for size in input_sizes:
        execution_time = measure_algorithm_time(size)
        times.append(execution_time)
        print(f"Размер: {size}, Время: {execution_time:.6f}s")

    plt.figure(figsize=(12, 8))
    plt.plot(input_sizes, times, marker='o', linewidth=2, markersize=8, color='red')

    plt.title('Зависимость времени выполнения алгоритма от размера входных данных',
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Размер входных данных (количество элементов)', fontsize=14)
    plt.ylabel('Время выполнения (секунды)', fontsize=14)

    plt.grid(True, alpha=0.3)

    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    create_performance_chart()



