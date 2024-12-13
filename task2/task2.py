import sys
import math

def read_circle(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        x, y = map(float, lines[0].split())
        radius = float(lines[1])
    return (x, y, radius)

def read_points(file_path):
    with open(file_path, 'r') as file:
        points = [tuple(map(float, line.split())) for line in file]
    return points

def check_point_position(circle, point):
    cx, cy, radius = circle
    px, py = point

    distance = math.sqrt((px - cx) ** 2 + (py - cy) ** 2)

    if math.isclose(distance, radius, rel_tol=1e-9):
        return 0  # Точка на окружности
    elif distance < radius:
        return 1  # Точка внутри
    else:
        return 2  # Точка снаружи

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <circle_file> <points_file>")
        sys.exit(1)

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    try:
        circle = read_circle(circle_file)
        points = read_points(points_file)
    except Exception as e:
        print(f"Error reading files: {e}")
        sys.exit(1)

    for point in points:
        position = check_point_position(circle, point)
        print(position)

if __name__ == "__main__":
    main()