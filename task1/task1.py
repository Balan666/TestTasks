import sys

def circular_array_path(n, m):
    circular_array = list(range(1, n + 1))

    path = []
    current_index = 0

    for _ in range(n):
        path.append(circular_array[current_index])
        current_index = (current_index + m - 1) % n
        if current_index == 0:
            break

    return ''.join(map(str, path))

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python script.py <n> <m>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
    except ValueError:
        print("Both arguments must be integers.")
        sys.exit(1)

    result = circular_array_path(n, m)
    print(result)
