import bisect
import matplotlib.pyplot as plt
import numpy as np

def choise_of_pointers(N, M, K, not_free):
    not_free = sorted(not_free) # сортирую список занятых точек
    free = [i for i in range(N) if i not in not_free] # тут свободные точки
    positions = [] # сюда буду записывать позиции

    for _ in range(K):
        max_len_between = 0 # макс расстояние м/у точками
        best_pos = 0 # лучшая позиция
        for i in range(len(not_free)):
            current = not_free[i] # текущая и -->
            after_cerrent = not_free[(i + 1) % M] # след. занятая точки
            len_between = (after_cerrent - current) % N # расстояние м/у ними
            # after_cerrent = not_free[(i + 1) % len(not_free)]
            if len_between > max_len_between:
                max_len_between = len_between
                best_pos = (current + len_between // 2) % N # лучшая позиция посередине промежутка

        # Проверяем, что best_pos находится в списке свободных точек
        if best_pos in free:
            positions.append(best_pos) # d cgbcjr gjpbwbq
            bisect.insort(not_free, best_pos) # в сортир. список точек
            free.remove(best_pos) # и удаляем из свободных
        else:
            # Если best_pos уже занят, ищем ближайшую свободную точку
            for pos in sorted(free, key=lambda x: abs(x - best_pos)):
                if pos in free:
                    positions.append(pos)
                    bisect.insort(not_free, pos)
                    free.remove(pos)
                    break

    return sorted(positions)

def plot_points(N, not_free, new_positions):
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False)
    x = np.cos(angles)
    y = np.sin(angles)

    fig, ax = plt.subplots()

    # Занятые точки, с которых начали мы
    ax.scatter([x[i] for i in not_free], [y[i] for i in not_free], c='blue', label='Занятые точки (M)')

    # Новые точки K
    ax.scatter([x[i] for i in new_positions], [y[i] for i in new_positions], c='green', label='Новые точки (K)')

    # Свободные точки
    free_points = [i for i in range(N) if i not in not_free and i not in new_positions]
    ax.scatter([x[i] for i in free_points], [y[i] for i in free_points], c='gray', label='Свободные точки', alpha=0.5)

    # Подписи точек
    for i in range(N):
        ax.text(x[i] * 1.1, y[i] * 1.1, str(i), fontsize=12, ha='center', va='center')

    ax.set_aspect('equal')
    plt.legend()
    plt.title('Распределение точек на окружности')
    plt.show()

# входные данные
N = 8
M = 4
K = 2
not_free = [0, 2, 4, 6]

new_positions = choise_of_pointers(N, M, K, not_free)
print("Новые позиции для объектов:", new_positions)

plot_points(N, not_free, new_positions)