import sys

MAX_HEADS = 7  # максимум голов у одного дракона


def max_power(n: int, max_heads: int = MAX_HEADS) -> int:
    """Возвращает максимальную силу стаи из n голов."""
    best = [1] * (n + 1)
    for s in range(1, n + 1):
        limit = min(max_heads, s)  # сколько голов может быть у дракона
        best[s] = max(k * best[s - k] for k in range(1, limit + 1))
    return best[n]


def read_heads() -> int:
    """Запрашивает число голов, пока не введено N от 1 до 99."""
    while True:
        text = input("Введите количество голов N (от 1 до 99): ").strip()
        try:
            n = int(text)
        except ValueError:
            print("Ошибка: нужно ввести натуральное число.")
            continue
        if 0 < n < 100:
            return n
        print("Ошибка: должно выполняться условие 0 < N < 100.")


def main() -> None:
    n = read_heads()
    print("Максимальная сила стаи:", max_power(n))


if __name__ == "__main__":
    main()
    if sys.stdin.isatty():  # чтобы окно не закрылось сразу после ответа
        input("Нажмите Enter, чтобы закрыть программу...")
